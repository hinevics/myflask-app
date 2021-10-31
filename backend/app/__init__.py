from flask import Flask
from flask_mongoengine import MongoEngine

from app import dev_settings


server = Flask(__name__)
server.config['MONGODB_SETTINGS'] = {
    'db': dev_settings.MONGO_DATABASE,
    'host': dev_settings.MONGO_HOST,
    'port': dev_settings.MONGO_PORT
}

db = MongoEngine()
db.init_app(server)

from app import models, routes

server.run()
