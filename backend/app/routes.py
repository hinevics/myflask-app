import json

from flask import render_template, redirect, url_for, request
from bson import json_util

from  app.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT
from app import server, collections
from app.print_top import create_plot


@server.route('/', methods=['GET'])
def start():
    
    # # return render_template('index.html')
    # # return user
    all_r = list(collections.find({}))
    return json.dumps(all_r, default=json_util.default)

@server.route('/top')
def top():
    return render_template('top.html', vartest=[f'Топовый автор #{i}' for i in range(10)])


@server.route('/distribution')
def distribution():
    bar = create_plot()
    return render_template('distribution.html', plot=bar)
