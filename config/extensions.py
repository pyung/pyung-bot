# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from logging.handlers import RotatingFileHandler

from flask_restful import Api
from flask_wtf.csrf import CSRFProtect

csrf_protect = CSRFProtect()
api = Api()
handler = RotatingFileHandler('log.log', maxBytes=10000, backupCount=1)
