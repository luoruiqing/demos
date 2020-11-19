from django.test import TestCase
from utils import error


class MTDMiddlewareTestCase(TestCase):
    def test_json_response(self):
        ''' 字典类型响应'''
        response = self.client.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'code': 200, 'message': 'success', 'data': {'status': 'ok'}})

    def test_model_response(self):
        ''' Django模型响应 '''
        response = self.client.get('/test?model=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()['data']), list)

    def test_assert_response(self):
        ''' 断言中断响应 '''
        response = self.client.get('/test?assert=1')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['code'], error.FILE_NOT_FOUND_ERROR.code)
