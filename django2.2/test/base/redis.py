from django.test import TestCase
from django_redis import get_redis_connection
from django.core.cache import cache
from unittest import TestCase
from utils.redis import _TEST_PATTERN


class RedisTestCase(TestCase):
    def test_connect(self):
        ''' Redis 连接测试'''
        key = "__TEST:CONNECT"
        self.assertTrue(cache.set(key, "value", timeout=25))
        self.assertTrue(cache.ttl(key) <= 25)

    def test_lock(self):
        ''' redis 锁功能是否正常 '''
        key = "__TEST:LOCK"
        with cache.lock(key):
            self.assertIn(key, cache.keys(f'{key}*'))
        self.assertNotIn(key, cache.keys(f'{key}*'))

    def test_cache_key(self):
        ''' 测试自定义Key是否可以使用 '''
        key1, value1 = _TEST_PATTERN('custom_1'), 'Test String 1.'
        key2, value2 = _TEST_PATTERN('custom_2'), {'test': 1}
        self.assertEqual(key1.value, None)
        self.assertEqual(key2.value, None)
        if not key1.value:
            key1.value = value1
        if not key2.value:
            key2.value = value2
        # 设置成功检查
        self.assertEqual(key1.value, value1)
        self.assertEqual(key2.value, value2)
        # 新建对象检查
        self.assertEqual(_TEST_PATTERN('custom_1').value, value1)
        # 在结果内
        self.assertIn(key1.key, _TEST_PATTERN.keys())
        self.assertIn(key2.key, _TEST_PATTERN.keys())
        # 删除 键1
        del key1.value
        self.assertEqual(key1.value, None)
        # 删除了一个键
        self.assertNotIn(key1.key, _TEST_PATTERN.keys())
        self.assertIn(key2.key, _TEST_PATTERN.keys())
        # 测试字典多次加载
        print(key2.value['test'])
        self.assertEqual(key2.value.copy(), value2)
        # 清空
        _TEST_PATTERN.clear()
        self.assertNotIn(key2.key, _TEST_PATTERN.keys())
