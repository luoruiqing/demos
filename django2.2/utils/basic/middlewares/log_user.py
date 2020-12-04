import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('django')


class LoggingUserMiddleware(MiddlewareMixin):
    ''' 日志打印用户 '''
    REQUEST_KEYS = ['scheme', 'method', 'path', 'session', 'META', 'COOKIES']

    def process_request(self, request):
        try:
            data = [
                request.user.id,
                request.user.first_name,
                request.user.last_login,
                request.META,
                request.COOKIES,
                # request.session,
            ]
            logger.info(' '.join(map(str, data)))
        except:
            pass
