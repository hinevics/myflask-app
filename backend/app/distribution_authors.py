from os import F_OK, terminal_size
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import random
from bson import json_util

from app import db_collections


def get_distribution_authors():
    result_find = db_collections.find({}, {'datecreate': True, '_id': True})
    data = [dict(datecreate=i['datecreate'], _id=str(i['_id'])) for i in list(result_find)]
    data = sorted(data, key=lambda x:x['datecreate'])
    graphJSON = json.dumps(data, default=json_util)
    return graphJSON