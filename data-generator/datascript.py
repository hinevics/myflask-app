import requests
import random
import datetime
import time

from pymongo import MongoClient

from config import MONGO_NUMBER_AUTHOR, MONGO_NUMBER_PAGE, \
    MONGO_DATABASE, MONGO_COLLECTION, MONGO_HOST, MONGO_PORT, API_FISH_TEXT, API_NAME


def name_generator(number_author: int, api_name: str) -> str:
    """[summary]

    Args:
        number_author (int): [description]
        api_name (str): [description]

    Returns:
        str: [description]
    """
    names = [requests.get(url=api_name).json()['name'] for _ in range(number_author)]
    return names


def text_generator(api_text: str):
    """[summary]

    Args:
        api_text (str): [description]

    Returns:
        [type]: [description]
    """
    return requests.get(url=api_text).json()['text']


def date_generator(number_page: int) -> list:
    """[summary]

    Args:
        number_page (int): [description]

    Returns:
        list: [description]
    """
    # datetime.date.today() - datetime.timedelta(DEFAULT_TIMEDELTA)
    result = [
        int(
            time.mktime(
                (datetime.datetime.today()-datetime.timedelta(
                    days=random.randint(a=1, b=i+1)*random.randint(a=1, b=i+1))).timetuple()))
        for i in range(number_page)]
    return result


def generation(number_author: int, number_page: int, api_name: str, api_text: str) -> dict:
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
    date = date_generator(number_page=number_page)
    for _ in range(number_page):
        name = names[random.randint(a=0, b=number_author-1)]
        yield dict(author=name, text=text_generator(api_text=api_text),
                   datecreate=date[random.randint(a=0, b=number_page-1)])


def create_utc(unixdatetime):
    utcdatetime = time.localtime(unixdatetime)
    return '{d}.{m}.{Y}'.format(d=utcdatetime.tm_mday, m=utcdatetime.tm_mon, Y=utcdatetime.tm_year)


def db_start():
    """[summary]
    """
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    db = client[MONGO_DATABASE]
    series_collection = db[MONGO_COLLECTION]

    # data = [{'author': 'Sasha', 'text':'yes'}, {'author': 'Sasha1', 'text':'yes1'}]
    data = [i for i in
            generation(number_author=MONGO_NUMBER_AUTHOR,
                       number_page=MONGO_NUMBER_PAGE, api_name=API_NAME, api_text=API_FISH_TEXT)]
    series_collection.insert_many(data)


def main():
    print('[Start of data creation]')
    db_start()
    print('[End of data creation]')


if __name__ == '__main__':
    main()
