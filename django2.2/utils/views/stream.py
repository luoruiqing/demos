
import functools
from os import path
from pathlib import Path

from django.http.response import StreamingHttpResponse
from django.utils.encoding import escape_uri_path

from .base import APIViewBase
from utils import error


class StreamView(APIViewBase):
    """ 二进制流式下载文件 """
    CHUNK_SIZE = 1024 * 256

    def _custom_process(func):
        @functools.wraps(func)
        def wrapper(self, request, *args, **kwargs):
            fileargs = func(self, request)
            filename, filepath = fileargs if isinstance(fileargs, tuple) and len(fileargs) == 2 else ('', fileargs)
            if isinstance(filepath, str) and Path(filepath).is_file():  # 文件
                iterator = self.binary_chunks(request, filepath)
                response = StreamingHttpResponse(iterator, content_type="application/octet-stream")
                response['Content-Disposition'] = 'attachment;filename={0}'.format(escape_uri_path(path.basename(filename or filepath)))  # 取文件名
                response['Content-Length'] = path.getsize(filepath)
                return response
            raise error.FILE_NOT_FOUND_ERROR(filepath)
        return wrapper

    def binary_chunks(self, request, file_path):
        """ 二进制块（按块） """
        with open(file_path, 'rb+') as f:
            chunk = f.read(self.CHUNK_SIZE)
            while chunk:
                yield chunk
                chunk = f.read(self.CHUNK_SIZE)
        self.close(request)

    def close(self, request):
        ''' 发送完成后要执行的内容 '''
