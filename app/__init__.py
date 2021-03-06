from flask import Flask
from config import Config
from app import rdbalchemy

app = Flask(__name__)
app.config.from_object(Config)
rdb = rdbalchemy.RDBAlchemy(Config.RDB_IP)

from app import route    