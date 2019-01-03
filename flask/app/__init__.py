# docker1/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config_dev')

db = SQLAlchemy(app)

from app import jinja, models, views