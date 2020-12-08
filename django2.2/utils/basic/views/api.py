import functools

from ..handler import APIHandler
from ..models import DjangoJSONEncoder
from .base import ViewBase


class APIViewBase(ViewBase):
    def wrapper_process(func):
        @functools.wraps(func)
        def wrapper(self, request, *args, **kwargs):
            handler = APIHandler()
            handler.JSONEncoder = getattr(self, 'JSONEncoder', handler.JSONEncoder)
            try:
                response = handler.process_request(request)
                if not response:
                    response = func(self, request, *args, **kwargs)
                response = handler.process_response(request, response)
            except Exception as e:
                response = handler.process_exception(request, e)
                if not response:
                    raise e
            return response
        return wrapper


class APIView(APIViewBase):
    JSONEncoder = DjangoJSONEncoder  # 切换序列化器
