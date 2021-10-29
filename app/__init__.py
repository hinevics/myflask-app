from flask import Flask
from flask_mongoengine import MongoEngine


server = Flask(__name__)
server.config['MONGODB_SETTINGS'] = {
    'db': 'database',
    'host':'localhost',
    'port':27017
    }
db = MongoEngine()
db.init_app(server)

from app import models, routes, print_top

server.run()
