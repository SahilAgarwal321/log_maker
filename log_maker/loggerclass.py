import logging
import configuration

class log1(object):

    # _instances = {}
    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls._instances:
    #         cls._instances[cls] = super(log1, cls).__call__(*args, **kwargs)
    #     return cls._instances[cls]

    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    VERSIONS_ALLOWED = ['1']
    LOG_TYPE_FILENAME_MAP = {
        'critical':'critical.log',
        'error': 'error.log',
        'warning': 'warning.log',
        'info': 'info.log',
        'debug': 'debug.log',
        'notset': 'notset.log'
    }

    # get_filename x: x + str(datetime.datetime.now().date()) + '.log'

    def __init__(self, log_type, log_msg):
        self.log_type = log_type
        self.log_msg = log_msg
        self._format = configuration.log_format
        self._filename = self.LOG_TYPE_FILENAME_MAP[self.log_type]
        self._filesuffix = configuration.filesuffix
        self._handler = configuration.handler
        self._level = configuration.level
        self._duration = configuration.duration
        self._backup = configuration.backup

    def log1(self):
        logger = logging.getLogger(self._filename)
        logger.setLevel(self._level)

        Handle = self._handler
        file_handler = Handle(self._filename, when=self._duration, backupCount=self._backup)
        file_handler.setLevel(self._level)
        file_handler.setFormatter(self._format)
        file_handler.suffix = self._filesuffix


        logger.addHandler(file_handler)
        getattr(logger, self.log_type)(self.log_msg)

# class Logger(object):
    # __metaclass__ = log1
