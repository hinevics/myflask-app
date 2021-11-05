import json

from flask import render_template, redirect, url_for, request

from  app.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT
from app import server, db_collections
from app.authors import authors_get_top
from app.distribution_authors import get_distribution_authors


@server.route('/')
def start():
    return render_template('index.html')


@server.route("/get_top", methods=['GET'])
def get_top():
    # добавить описание что мол как получить json
    return authors_get_top()


@server.route('/render_top', methods=['GET'])
def render_top():
# возможность выбирать какой топ хочу... 
    top_authors = json.loads(s=authors_get_top())
    return render_template('top.html', vartest=[f'Top number #{i[0] + 1}: {i[1]["author"]}' for i in enumerate(top_authors)])


@server.route('/get_distribution', methods=['GET'])
def get_distribution():
    return get_distribution_authors()


@server.route('/distribution', methods=['GET'])
def distribution():
    bar = get_distribution_authors()
    return render_template('distribution.html', plot=bar)
