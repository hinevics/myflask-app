import requests
import random

from pymongo import MongoClient

from app.config import MONGO_NUMBER_AUTHOR, MONGO_NUMBER_PAGE,\
MONGO_DATABASE, MONGO_COLLECTION, MONGO_HOST, MONGO_PORT, API_FISH_TEXT, API_NAME


def name_generator(number_author:int, api_name:str) -> str:
    """[summary]

    Args:
        number_author (int): [description]
        api_name (str): [description]

    Returns:
        str: [description]
    """
    names = [requests.get(url=api_name).json()['name'] for i in range(number_author)]
    
    return names

def text_generator(api_text:str):
    """[summary]

    Args:
        api_text (str): [description]

    Returns:
        [type]: [description]
    """
    return requests.get(url=api_text).json()['text']


def generation(number_author:int, number_page:int, api_name:str, api_text:str) -> dict:
    """[summary]

    Args:
        number_author (int): [description]
        number_page (int): [description]
        api_name (str): [description]
        api_text (str): [description]

    Returns:
        dict: [description]

    Yields:
        Iterator[dict]: [description]
    """
    names = name_generator(number_author=number_author, api_name=api_name)
    
    for i in range(number_page):
        name = names[random.randint(a=0, b=number_author-1)]
        yield dict(author=name, text=text_generator(api_text=api_text))

def db_start():
    """[summary]
    """
    print('start create db')
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    db = client[MONGO_DATABASE]
    series_collection = db[MONGO_COLLECTION]

    # data = [{'author': 'Sasha', 'text':'yes'}, {'author': 'Sasha1', 'text':'yes1'}]
    series_collection.drop() # Это нужно только тут, те убрать в контейнере !!!!!
    data = [i for i in
            generation(number_author=MONGO_NUMBER_AUTHOR, number_page=MONGO_NUMBER_PAGE, api_name=API_NAME, api_text=API_FISH_TEXT)]
    series_collection.insert_many(data)
    print('end create db')


def main():
    from collections import Counter

    db_start()
    a = input()
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    db = client[MONGO_DATABASE]
    series_collection = db[MONGO_COLLECTION]
    authors = [i['author'] for i in list(series_collection.find({}, {'author': True, '_id':False}))]
    print([(element, count) for element, count in Counter(authors).most_common()])

if __name__ == '__main__':
    main()
