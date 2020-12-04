import json
import logging
from django.http.response import HttpResponseBase, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from ..models import DjangoJSONEncoder
from .. import error


class MiddlewareMixinBase(MiddlewareMixin):
    ''' 基础中间件, 用于请求前JSON校验, 响应后格式统一, 错误后格式统一 '''
    DEFAULT_RESPONSE_JSON = {"code": 200, 'message': "success"}

    JSONEncoder = json.JSONEncoder  # json转换器

    def process_request(self, request):
        request_json = 'application/json' in request.META.get('HTTP_ACCEPT', '')
        try:  # 增加JSON
            request.json = json.loads(request.body) if request_json and request.body else {}
        except Exception as e:  # 提交json错误
            logging.error(f'{error.REQUEST_JSON_ERROR} -> {request.body}')
            raise error.REQUEST_JSON_ERROR

    def process_response(self, request, response):
        if isinstance(response, HttpResponseBase):  # 正常响应对象
            return response

        data = json.dumps({**self.DEFAULT_RESPONSE_JSON.copy(), **{'data': response}}, cls=self.JSONEncoder)
        return HttpResponse(data, content_type='application/json')

    def process_exception(self, request, e):
        e = (isinstance(e, AssertionError) and isinstance(e.args[0], error.BaseError) and e.args[0]) or e
        # 处理已知错误
        if isinstance(e, error.BaseError):
            return HttpResponse(json.dumps({"code": e.code, 'message': e.message}), status=e.status_code, content_type='application/json')


class MTDMiddleware(MiddlewareMixinBase):
    ''' 模型转换支持 '''
    JSONEncoder = DjangoJSONEncoder
