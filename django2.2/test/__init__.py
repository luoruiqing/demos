from .base.middleware import MTDMiddlewareTestCase
from .base.sse import SSETestCase
from .chat import ChannelsRedisConnectTestCase
if __name__ == '__main__':
    ChannelsRedisConnectTestCase.main()
    MTDMiddlewareTestCase.main()
    SSETestCase.main()
