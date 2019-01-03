# docker1/config_dev.py

import os

# SQLAlchemy

SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

SQLALCHEMY_TRACK_MODIFICATIONS = True