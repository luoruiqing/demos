from .base import GrapDjangoModelEnumBase


class GrapEnumQuery(GrapDjangoModelEnumBase):
    ''' 枚举查询 '''

    def executor(self, info, args, **kwargs):
        return self.attrs


