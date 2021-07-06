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

from app import routes, models