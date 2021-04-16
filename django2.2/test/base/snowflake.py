from django.test import TestCase
from django_redis import get_redis_connection
from django.core.cache import cache
from unittest import TestCase
from utils import redis


class SnowflakeTestCase(TestCase):
    def test_get_id(self):
        '''
        测试获取雪花算法的 ID 
        pip install pysnowflake && snowflake_start_server --address=0.0.0.0 --port=8910 --dc=1 --worker=1 --log_file_prefix=/tmp/pysnowflask.log # 启动雪花算法服务
        '''
        import snowflake.client
        self.assertEqual(snowflake.client.get_stats()['errors'], 0)
        id = str(snowflake.client.get_guid())
        self.assertEqual(len(str(id)), 19)

