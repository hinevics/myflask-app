from collections import Counter
from bson import json_util
import json

from app import db_collections

def authors_get_top() -> list:
    """[summary]

    Returns:
        list: [description]
    """
    authors = [i['author'] for i in list(db_collections.find({}, {'author': True, '_id':False}))]
    result = json.dumps([{'author': element, 'count': count} for element, count in Counter(authors).most_common()], default=json_util)
    return result