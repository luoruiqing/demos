'''
视图基类
'''
from django.views.generic import View


class APIViewBase(View):
    '''  自定义视图基类 '''

    @staticmethod
    def _custom_process(func):
        ''' 这是装饰器方法, 用于实现响应 '''
        raise NotImplementedError()

    def __init_subclass__(cls, **kwargs):
        ''' 利用 __init_subclass__ 方法, 给请求方法进行装饰 '''
        if next(filter(lambda c: issubclass(c, APIViewBase), cls.__mro__), None):  # 正确的继承
            for method in cls.http_method_names:  # 针对Django View的装饰
                if hasattr(cls, method):
                    setattr(cls, method, cls._custom_process(getattr(cls, method)))
        return super(cls).__init_subclass__(**kwargs)
