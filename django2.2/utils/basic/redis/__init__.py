from django_redis import get_redis_connection
from .cache_key import key, _TEST_PATTERN

redis = get_redis_connection("default")
Key = key
