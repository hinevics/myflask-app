import json

from flask import render_template, redirect, url_for, request
from bson import json_util

import app.config as config
from app import server
from app.models import User
from app.print_top import create_plot

@server.route('/', methods=['GET'])
def start():
    user = User.objects(author='Саша').first()
    # return render_template('index.html')
    return user
    # return json.dumps(a, default=json_util.default)

@server.route('/top')
def top():
    return render_template('top.html', vartest=[f'Топовый автор #{i}' for i in range(10)])


@server.route('/distribution')
def distribution():
    bar = create_plot()
    return render_template('distribution.html', plot=bar)
