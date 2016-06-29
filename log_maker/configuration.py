import logging
from logging.handlers import TimedRotatingFileHandler

log_format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s in %(pathname)s:%(funcName)s:%(lineno)d')
# filename = 'app.log'
filesuffix = '%Y-%m-%d'
handler = TimedRotatingFileHandler
level = logging.NOTSET
duration = 'D'
backup = 30