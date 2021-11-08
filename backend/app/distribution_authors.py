import time
import datetime
from collections import Counter
import json
import random
from bson import json_util

import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from app import db_collections
from app.config import MONGO_NUMBER_DAY

def get_distribution_authors():
    # result_find = db_collections.find({}, {'datecreate': True, '_id': True})
    # data = [dict(datecreate=i['datecreate'], _id=str(i['_id'])) for i in list(result_find)]
    # data = sorted(data, key=lambda x:x['datecreate'])
    # graphJSON = (data, default=json_util)
    # return graphJSON
    data = list(db_collections.find({}, {'author':True, 'datecreate':True}))
    delta_today = int(time.mktime((datetime.datetime.today() - datetime.timedelta(days=MONGO_NUMBER_DAY*30)).timetuple()))
    result = Counter([i['author'] for i in data if i['datecreate'] > delta_today])
    # x, y = result.keys(), result.values()
    return json.dumps([dict(author=i, count=j) for i, j in result.items()], default=json_util)
    