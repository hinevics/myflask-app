from flask import render_template, redirect, url_for, request

from app import server
from app.models import User
from app.print_top import create_plot
from app.datageneration import generation

@server.route('/', methods=['GET'])
def start():
    generation()
    return render_template('index.html')

@server.route('/top')
def top():
    return render_template('top.html', vartest=[f'Топовый автор #{i}' for i in range(10)])


@server.route('/distribution')
def distribution():
    bar = create_plot()
    return render_template('distribution.html', plot=bar)
