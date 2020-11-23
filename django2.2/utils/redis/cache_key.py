'''
使用方式:

_TEST_PATTERN = key('__TEST:PATTERN:{}', 10)  # 定义

sub_key = _TEST_PATTERN('sub')     # 生成子键
if not sub_key.value:              # 判断缓存不存在
    sub_key.value = 'test data'    # 设置缓存

'''
from django.core.cache import cache


class Value:
    ''' 描述符用于值代理, 属于本地变量, 不可以要求实时性 '''

    def __get__(self, instance, owner):
        ''' 优先本地, 否则取数据库 '''
        instance._v = getattr(instance, '_v', None) or cache.get(instance.key)
        return instance._v

    def __set__(self, instance, value):
        ''' 数据库同步更新 '''
        instance._v = value
        return cache.set(instance.key, value, timeout=instance.expire)

    def __delete__(self, instance):
        ''' 数据库同步删除 '''
        instance._v = None
        return cache.delete(instance.key)


class CacheKey:
    PATTERNS = {}  # 所有模式
    value = Value()

    def __init__(self, *args, **kwargs):
        self.key = self.pattern.format(*args, **kwargs)

    @classmethod
    def keys(cls):
        return cache.keys(cls.character)

    @classmethod
    def clear(cls):
        return cache.delete_pattern(cls.character)


def key(pattern, expire):
    cache_key = type('NewCacheKey', (CacheKey,), {
        'pattern': pattern, 'expire': expire, 'character': f'{pattern.split("{", 1)[0]}*'
    })
    assert pattern not in CacheKey.PATTERNS, f"Cache Pattern duplication: {pattern}."
    CacheKey.PATTERNS[pattern] = cache_key
    return cache_key


_TEST_PATTERN = key('__TEST:PATTERN:{}', 10)
