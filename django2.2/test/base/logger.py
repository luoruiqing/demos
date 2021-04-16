from django.test import TestCase
import logging


class LoggerTestCase(TestCase):
    def test_logger(self):
        if hasattr(logging, 'notset'):
            logging.notset('这是 DEBUG 消息')
        logging.debug('这是 DEBUG 消息')
        logging.info('这是 info 消息')
        logging.warning('这是 WARNING 消息')
        logging.error('这是 ERROR 消息')
        logging.fatal('这是 FATAL 消息 ')
        logging.critical('这是 CRITICAL 消息')
