from flask import Flask

appName = Flask(__name__)

from app import routes
