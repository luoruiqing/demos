from django.utils.deprecation import MiddlewareMixin

from ..handler import APIHandler
from ..models import DjangoJSONEncoder


class APIMiddlewareMixinBase(MiddlewareMixin, APIHandler):
    pass


class APIMiddleware(APIMiddlewareMixinBase):
    JSONEncoder = DjangoJSONEncoder
