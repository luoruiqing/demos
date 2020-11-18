'''
自定义错误模块, 支持code码唯一, 和多次调用及参数格式化
'''


class BaseError(BaseException):
    """ 自定义错误基类 """
    CODES = {}  # 所有错误


class Error(BaseError):
    ''' 自定义错误类 '''
    status_code = 400  # 默认错误响应状态码
    code = None  # 错误代码
    message = ''  # 错误消息

    def __new__(cls, code, *args, **kwargs):
        check = kwargs.pop('check', True)
        instance = super().__new__(cls, code, *args, **kwargs)
        if check:
            assert code not in instance.CODES, f"Error code duplication: {code}."
            instance.CODES[code] = instance  # 记录错误实例
        return instance

    def __init__(self, code, message, status_code=400, *args, **kwargs):
        ''' 带参数进入格式化到消息体 '''
        self.code = code
        self.message = message
        self.status_code = status_code

    def __call__(self, *args, **kwargs):
        ''' 回调始终生成新的错误对象, 且code不允许变化 '''
        message = (self.message.format(*args, **kwargs)) if args or kwargs else self.message

        return self.__class__(
            code=self.code,
            message=message,
            status_code=self.status_code,
            check=False,
        )

    def __str__(self):
        return f'Error {self.code}({self.status_code}): {self.message}.'


REQUEST_JSON_ERROR = Error(10000, 'JSON请求不合法. {}')

if __name__ == "__main__":
    import unittest

    class TestDemo(unittest.TestCase):
        ''' 单元测试 '''

        def tearDown(self):
            Error.CODES.clear()  # 清除

        def test_error_code_duplication(self):
            ''' 测试错误代码重复 '''
            ERROR1 = Error(10000, '这是个错误! {}')
            with self.assertRaises(AssertionError):
                ERROR2 = Error(10000, '这是个错误! {}')

        def test_error_repeat_call(self):
            ''' 测试多次调用同一实例 '''
            ERROR1 = Error(10000, '这是个错误! {}')
            temporary_error_1 = ERROR1('附加信息1')
            self.assertEqual(temporary_error_1.code, 10000)
            self.assertEqual(temporary_error_1.message, '这是个错误! 附加信息1')
            temporary_error_2 = temporary_error_1('附加信息2')
            self.assertEqual(temporary_error_2.code, 10000)
            self.assertEqual(temporary_error_2.message, '这是个错误! 附加信息1')

        def test_error_type_checking(self):
            ''' 测试实例类型 '''
            ERROR1 = Error(10000, '这是个错误! {}')
            self.assertIsInstance(ERROR1, Error)
            temporary_error_1 = ERROR1('附加信息1')
            self.assertIsInstance(temporary_error_1, Error)
            temporary_error_2 = temporary_error_1('附加信息2')
            self.assertIsInstance(temporary_error_2, Error)

            self.assertTrue(issubclass(ERROR1.__class__, BaseError))

    unittest.main()
