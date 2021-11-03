from collections import Counter

from app import db_collections

def authors_get_top() -> list:
    """[summary]

    Returns:
        list: [description]
    """
    authors = [i['author'] for i in list(db_collections.find({}, {'author': True, '_id':False}))]
    result = [{'author': element, 'count': count} for element, count in Counter(authors).most_common()]
    return result