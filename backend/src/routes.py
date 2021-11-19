from flask import render_template

# from  app.config import MONGO_COLLECTION, MONGO_DATABASE, MONGO_HOST, MONGO_PORT
from src import server
from src.authors import authors_get_top, top_authors_render, get_distribution_authors


@server.route('/')
def start():
    return render_template('index.html')


@server.route("/api/v1/authors/top", methods=['GET'])
def get_top():
    return authors_get_top()


@server.route('/top', methods=['GET'])
def render_top():
    return render_template('top.html', vartest=top_authors_render())


@server.route('/api/v1/authors/distribution', methods=['GET'])
def get_distribution():
    return get_distribution_authors()


@server.route('/distribution', methods=['GET'])
def render_distribution():
    bar = get_distribution_authors()
    return render_template('distribution.html', plot=bar)
