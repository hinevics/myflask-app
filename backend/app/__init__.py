from flask import Flask
from flask_mongoengine import MongoEngine

import app.config as config
from app.datascript import dbstart

dbstart()

print('start create flask app')
server = Flask(__name__)
server.config['MONGODB_SETTINGS'] = {
    'db': config.MONGO_DATABASE,
    'host': config.MONGO_HOST,
    'port': config.MONGO_PORT
}

db = MongoEngine()
db.init_app(server)
from app import routes, config, print_top

server.run()
