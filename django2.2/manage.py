#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1:3] == ['celery', 'worker']:
        ''' 针对celery worker的补丁(未经过大量测试) '''
        from kombu.transport.redis import QoS, dumps, time

        def append(self, message, delivery_tag):
            delivery = message.delivery_info
            EX, RK = delivery['exchange'], delivery['routing_key']
            with self.pipe_or_acquire() as pipe:
                pipe.zadd(self.unacked_index_key, {delivery_tag: time()}) \
                    .hset(self.unacked_key, delivery_tag,
                          dumps([message._raw, EX, RK])) \
                    .execute()
                super(QoS, self).append(message, delivery_tag)
        setattr(QoS, 'append', append)
    main()
