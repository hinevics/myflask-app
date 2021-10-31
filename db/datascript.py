import os
import requests
from config import MONGO_HOST
# from pymongo import MongoClient

# from db.tools.datageneration import generation
# from db.dev_settings import MONGO_NUMBER, MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_COLLECTION

print(MONGO_HOST)

# API_FISH_TEXT = r'https://fish-text.ru/get?format=json&number=5'
# API_NAME = r'https://api.namefake.com/'


# def name_generator():
#     return requests.get(url=API_NAME).json()['name']


# def text_generator():
#     return requests.get(url=API_FISH_TEXT).json()['text']


# def generation(number):
#     for i in range(number):
#         yield dict(author=name_generator(), text=text_generator())

# client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
# db = client[MONGO_DATABASE]
# series_collection = db[MONGO_COLLECTION]
# data = [i for i in generation(MONGO_NUMBER)]
# series_collection.insert_many(data)