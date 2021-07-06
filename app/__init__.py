from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

appName = Flask(__name__)

login = LoginManager(appName)
login.login_view = 'login'

appName.config.from_object(Config)

db = SQLAlchemy(appName)
migrate = Migrate(appName, db)

from app import routes, models, errors

import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os

if not appName.debug:
    if appName.config['MAIL_SERVER']:
        auth = None
        if appName.config['MAIL_USERNAME'] or appName.config['MAIL_PASSWORD']:
            auth = (appName.config['MAIL_USERNAME'], appName.config['MAIL_PASSWORD'])
        secure = None
        if appName.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(appName.config['MAIL_SERVER'], appName.config['MAIL_PORT']),
            fromaddr='no-reply@' + appName.config['MAIL_SERVER'],
            toaddrs=appName.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        appName.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    appName.logger.addHandler(file_handler)

    appName.logger.setLevel(logging.INFO)
    appName.logger.info('Microblog startup')