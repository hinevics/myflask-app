import os

from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')
MONGO_NUMBER_AUTHOR = int(os.getenv('MONGO_NUMBER_AUTHOR'))
MONGO_NUMBER_PAGE = int(os.getenv('MONGO_NUMBER_PAGE'))
MONGO_NUMBER_DAY = int(os.getenv('MONGO_NUMBER_DAY'))
API_NAME = os.getenv('API_NAME')
API_FISH_TEXT = os.getenv('API_FISH_TEXT')