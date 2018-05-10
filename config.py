import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    RDB_IP = os.environ.get('RDB_IP') or '124.0.0.11'
