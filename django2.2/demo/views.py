from django.views.generic import View
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.views import View
from django.http import HttpResponse
from utils import error


class TestView(View):
    def get(self, request):
        ''' 
        http://localhost:8000/test?assert=1&assert_arg=yes # 错误参数格式化
        http://localhost:8000/test?assert=1 # 开启断言错误
        http://localhost:8000/test # 对象返回
        '''
        if request.GET.get('assert'):
            assert_arg = request.GET.get('assert_arg')
            if assert_arg:
                assert False, error.REQUEST_JSON_ERROR(assert_arg)
            assert False, error.REQUEST_JSON_ERROR
        if request.GET.get('model'):
            return ContentType.objects.all()
        return {
            "status": 'ok',
        }
