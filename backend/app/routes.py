import json

from flask import render_template, redirect, url_for, request
from bson import json_util

from  app.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT
from app import server, db_collections
from app.authors import authors_get_top
from app.distribution_authors import create_plot

@server.route('/')
def start():
    return render_template('index.html')


@server.route("/get_top", methods=['GET'])
def get_top():
    return json.dumps(authors_get_top(),default=json_util)


@server.route('/render_top', methods=['GET'])
def render_top():
    top_authors = json.loads(s=get_top())
    return render_template('top.html', vartest=[f'Top number #{i[0] + 1}: {i[1]["author"]}' for i in enumerate(top_authors)])


@server.route('/distribution')
def distribution():
    bar = create_plot()
    return render_template('distribution.html', plot=bar)
