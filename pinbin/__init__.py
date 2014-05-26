from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
import os, re
from util import MongoHQURL

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "pinbin"}
app.config["SECRET_KEY"] = "HIMOM"
app.config["MAPBOX_KEY"] = os.environ.get("MAPBOX_KEY")
DEBUG = os.environ.get("DEBUG")
MONGO_URL = os.environ.get("MONGOHQ_URL")

if MONGO_URL:
  con_obj = MongoHQURL(MONGO_URL)
  connect(con_obj.database, username=con_obj.username, password=con_obj.password, port=int(con_obj.port), host=con_obj.host)


app.debug = True

db = MongoEngine(app)

# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)

import views

if __name__ == '__main__':
    app.run()
