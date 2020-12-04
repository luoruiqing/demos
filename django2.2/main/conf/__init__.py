from .default import *  # 自定义地域/数据库/连接等配置
# -- 扩展
from .logs import *  # 日志配置及颜色扩展
from .graphql import *  # Graphql 扩展
from .celery import *  # 异步任务扩展
from .constance import *  # 程序读取动态配置
from .account import *  # 用户扩展
from .guardian import *  # 对象权限(行权限)
from .reversion import *  # 历史记录及回滚
from .taggit import *  # 标签系统
from .notifications import *  # 通知应用逻辑扩展(基于 Django 用户)
from .socket import *  # WebSocket 扩展及测试应用
from .debug_toolbar import *  # DEBUG 调试工具
# 测试应用
from .demo_app import *
