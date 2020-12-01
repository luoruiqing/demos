import functools
from .base import APIViewBase
from django.http.response import StreamingHttpResponse


class SSECloseStatus:
    ''' 用于关闭状态的检测 '''

    def __init__(self, request, callback=lambda: None):
        self.request = request
        self.callback = callback

    def __del__(self):
        return self.callback(self.request)


class SSEStreamBaseView(APIViewBase):
    ''' SSE 传输信息'''

    RETRY = 3000  # 重试间隔时间(毫秒)

    ACCESS_CONTROL_ALLOW_ORIGIN = '*'  # 是否允许跨域
    CONTENT_ENCODING = 'none'  # 内容编码 (默认关闭压缩)
    X_ACCEL_BUFFERING = 'no'  # Nginx关闭缓存设置

    def _custom_process(func):
        @functools.wraps(func)
        def wrapper(self, request, *args, **kwargs):
            response = StreamingHttpResponse(self.sse_iterator(func, request), content_type='text/event-stream')
            response['Cache-Control'] = 'no-cache'
            response['Connection'] = 'keep-alive'
            response['Content-Encoding'] = self.CONTENT_ENCODING
            response['Access-Control-Allow-Origin'] = self.ACCESS_CONTROL_ALLOW_ORIGIN
            response['X-Accel-Buffering'] = self.X_ACCEL_BUFFERING
            return response
        return wrapper

    def sse_iterator(self, func, request):
        ''' 符合协议的推送数据 '''
        yield f'retry: {self.RETRY}\n\n'
        # 这里是在第一条retry发生后再进行捕捉, 若服务未连接成功, 则不会调用close
        _ = SSECloseStatus(request, self.close)

        for event in func(self, request):
            yield f'data: {event}\n\n'

    def close(self, request):
        ''' 关闭客户端 '''
        raise NotImplementedError()


class SSEStreamView(SSEStreamBaseView):
    def close(self, request):
        ''' 关闭客户端不处理 '''
