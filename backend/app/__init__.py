from flask import Flask, app
from flask_mongoengine import MongoEngine

from pymongo import MongoClient

from app.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT
from app.datascript import dbstart

dbstart()

print('start create flask app')
server = Flask(__name__)


cluster = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = cluster[MONGO_DATABASE]
collections = db[MONGO_COLLECTION]

from app import routes, config, print_top

server.run()
