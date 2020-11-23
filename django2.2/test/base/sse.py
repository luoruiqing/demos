from django.test import TestCase
from utils import error
# from unittest import TestCase


class SSETestCase(TestCase):
    ''' '''
    # def test_sse(self):
    #     ''' 字典类型响应'''
    #     for index, message in enumerate(self.client.get('/test-sse')):
    #         if index > 3:
    #             break
    #         if index == 0:
    #             self.assertEqual(message[:5], b'retry')
    #         else:
    #             self.assertEqual(message[:4], b'data')
