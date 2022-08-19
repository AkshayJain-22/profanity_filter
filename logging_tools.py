import logging

from flask import Flask


class logger():
    def __init__(self,name=__name__) -> None:
        self.name = name
        self.app = Flask(name)
        gunicorn_logger = logging.getLogger('gunicorn.error')
        self.app.logger.handlers = gunicorn_logger.handlers
        self.app.logger.setLevel(gunicorn_logger.level)
    
    def log_error(self,message):
        self.app.logger.error(message)

    def log_info(self,message):
        self.app.logger.info(f'[{self.name}] : {message}') 