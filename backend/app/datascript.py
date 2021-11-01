import os
import requests
from pymongo import MongoClient

import app.config as config

def name_generator():
    return requests.get(url=config.API_NAME).json()['name']


def text_generator():
    return requests.get(url=config.API_FISH_TEXT).json()['text']


def generation(number):
    for i in range(number):
        yield dict(author=name_generator(), text=text_generator())

def dbstart():
    print('start create db')
    client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
    db = client[config.MONGO_DATABASE]
    series_collection = db[config.MONGO_COLLECTION]

    # data = [i for i in generation(config.MONGO_NUMBER)]
    data = [{'author': 'Саша', 'text':'yes'}]

    series_collection.insert_many(data)
    print('end create db')
