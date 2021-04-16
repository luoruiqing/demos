from .middleware import MTDMiddlewareTestCase
from .sse import SSETestCase
from .web_socket import WebSocketTestCase
from .redis import RedisTestCase
from .logger import LoggerTestCase
from .snowflake import SnowflakeTestCase

# from .base.database import *


def main():
    # 功能测试 ------------------------------------------------------------
    MTDMiddlewareTestCase.main()  # 中间件功能逻辑测试
    SSETestCase.main()  # SSE封装模块
    WebSocketTestCase.main()  # WebSocket测试
    # 下载模块测试
    # 基础服务测试 ------------------------------------------------------------
    #  数据库连接测试
    RedisTestCase.main()  # 缓存数据库
    LoggerTestCase.main()  # 日志颜色测试
    # SnowflakeTestCase.mian() # 雪花 ID 生成服务
    # 业务相关测试
