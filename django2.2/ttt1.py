
class Key(str):
    EXPIRE = 600
    # cache_key = type('NewCacheKey', (CacheKey,), {
    #     'pattern': pattern, 'expire': expire, 'character': f'{pattern.split("{", 1)[0]}*'
    # })

    def __init__(self, string, expire=None):
        print(string, expire)
        # self.expire = expire or self.EXPIRE
        # super().__init__()

    def format(self, *args, **kwargs):
        return self.__class__(super().format(*args, **kwargs))

    __call__ = format


key = Key('A:{}', 20)
key1 = key('123123:{}')
key2 = key1('ccc')
key3 = key2.format('123')
print(key, key1, key2, key3)
