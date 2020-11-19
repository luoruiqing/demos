from asgiref.sync import async_to_sync
import channels.layers


from django.test import TestCase
from utils import error


class ChannelsRedisConnectTestCase(TestCase):
    def test_channels_redis_connect(self):
        ''' WebSocket(Channels) 连接Redis测试 '''
        data = {'type': 'hello'}
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.send)('test_channel', data)
        result = async_to_sync(channel_layer.receive)('test_channel')
        self.assertDictEqual(data, result)
