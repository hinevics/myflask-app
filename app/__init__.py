from contextlib import closing
from flask import Flask
# from flask_mongoengine import MongoEngine
import pymongo

server = Flask(__name__)

try:
    mongo = pymongo.MongoClient(host='localhost', port=27017,
                            ServerSelectionTimeoutMS= 1000)
    db = mongo.company()
    mongo.server_info()
except:
    print('ERROR - cannot connect to db')
# server.config['MONGODB_SETTINGS'] = {
#     'db': 'database'}
# db = MongoEngine()
# db.init_app(server)

from app import models, routes, print_top

server.run()
