from flask import Flask
from flask.ext.mongoengine import MongoEngine
import os, re


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "pinbin"}
app.config["SECRET_KEY"] = "HIMOM"

MONGO_URL = os.environ.get("MONGOHQ_URL")

if MONGO_URL:
    credentials = re.sub(r"(.*?)//(.*?)(@hatch)", r"\2",MONGO_URL)
    username = credentials.split(":")[0]
    password = credentials.split(":")[1]
    app.config["MONGODB_DB"] = MONGO_URL.split("/")[-1]
    connect(
        MONGO_URL.split("/")[-1],
        host=MONGO_URL,
        port=1043,
        username=username,
        password=password
    )

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
