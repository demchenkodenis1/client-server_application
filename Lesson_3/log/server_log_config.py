import logging
from logging.handlers import TimedRotatingFileHandler

def handler_server_func(message_log, dir_way):
    logger = logging.getLogger('app_test.main')

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

    handler = logging.handlers.TimedRotatingFileHandler(+-
        filename=dir_way,
        when='H',
        interval=24,
        encoding='utf-8',
    )
    handler.suffix = '%Y-%m-%d'
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug(message_log)

def main():
    handler_server_func('Start test_test server', 'app.main.log')

if __name__ == '__main__':
    main()