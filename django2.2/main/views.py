import time
import logging

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.views import View
from django.views.generic import View
from utils import error, views

logger = logging.getLogger('django')


class TestView(View):
    '''
    http://localhost:8000/test?assert=1&assert_arg=yes # 错误参数格式化
    http://localhost:8000/test?assert=1 # 开启断言错误
    http://localhost:8000/test # 对象返回
    '''

    def get(self, request):
        if request.GET.get('assert'):
            assert_arg = request.GET.get('assert_arg')
            if assert_arg:
                assert False, error.FILE_NOT_FOUND_ERROR('assert_arg')
            assert False, error.FILE_NOT_FOUND_ERROR
        if request.GET.get('model'):
            return ContentType.objects.all()
        return {
            "status": 'ok',
        }


class TestStreamView(views.StreamView):
    '''
    http://localhost:8000/test-stream?filename=test.py # 双参数返回文件名和路径
    http://localhost:8000/test-stream # 只返回路径, 默认名称
    '''
    TEST_FILE = './main/views.py'

    def get(self, request):
        self.now = time.time()
        if request.GET.get('filename'):
            return request.GET.get('filename'), self.TEST_FILE
        return self.TEST_FILE

    def close(self, request):
        logger.info(f'{self.now} 时的下载已关闭.')


class TestSSEView(views.SSEStreamView):
    '''
    http://localhost:8000/test-sse
    '''

    def get(self, request):
        self.now = time.time()
        for i in range(100000):
            yield f'这是消息{i}.'
            time.sleep(0.5)

    def close(self, request):
        logger.info(f'{self.now} 时接入连接已关闭.')
