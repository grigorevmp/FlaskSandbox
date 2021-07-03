from flask import Flask
from config import Config

appName = Flask(__name__)
appName.config.from_object(Config)

from app import routes