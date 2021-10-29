import requests

from app.models import User


API_FISH_TEXT = r'https://fish-text.ru/get?format=json&number=5'
API_NAME = r'https://api.namefake.com/'


def name_generator():
    return requests.get(url=API_NAME).json()['name']


def text_generator():
    return requests.get(url=API_FISH_TEXT).json()['text']


def generation():
    for i in range(2):
        # user = User(author=name_generator(), text=text_generator())
        user = {'author':"A", 'text':'AAA'}
        user.save()