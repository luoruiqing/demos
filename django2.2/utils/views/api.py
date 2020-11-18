''' 全局默认视图 '''
import functools
import json
from django.conf import settings
# from collections import Iterable

from django.http.response import HttpResponseBase, HttpResponse
# from django.db.models import Model, QuerySet
# from django.http.response import HttpResponse, HttpResponseBase, StreamingHttpResponse

# from rest_framework.response import Response as RestfulResponse
# from .models import model_to_dict
from . import base
from .. import error


class APIView(base.APIViewBase):
    """ JSON接口处理 """
    JSONEncoder = json.JSONEncoder  # json转换器

    DEFAULT_RESPONSE_JSON = {"code": 200, 'message': "success", "data": {}}

    __init_subclass__ = base.__init_subclass__

    # def _custom_process_request(self, request, *args, **kwargs):
        

    # def _custom_process_response(self, response=None):
        

    # def _custom_process_error(self, response):
    #     if isinstance(e, AssertionError) and e.args:  # 通过断言抛出的已知错误
    #         if settings.BASE_DIR in e.__traceback__.tb_frame.f_globals['__file__']:  # 发生错误是服务提供所在目录
    #             e = e.args[0] if isinstance(e.args[0], error.BaseError) else error.Error(-1, e.args[0], check=False)
    #     # 处理已知错误
    #     if isinstance(e, error.BaseError):
    #         return HttpResponse(json.dumps({"code": e.code, 'message': e.message}), status=e.status_code, content_type='application/json')
    #     # 打印日志
    #     raise e

    @staticmethod
    def _custom_process(func):
        ''' 装饰器实现错误收集和数据类型转换, 以及断言处理 '''
        @functools.wraps(func)
        def wrapper(self, request, *args, **kwargs):
            # try:
            #     response = self._custom_process_request()

            #     if not response:
            #         response = func(self, request, *args, **kwargs)  # 获取响应对象
            #         response = self._custom_process_response(response) or response

            # except Exception as e:
            #     self._custom_process_error()
            print(self.process_request)
            return func(self, request)
        return wrapper
