from flask import render_template, redirect, url_for, request

from app import server
from app.models import User
from app.print_top import top_plot

@server.route('/')
def start():
    return render_template('index.html')

@server.route('/top')
def top():
    top_plot()
    return render_template('top.html', url='/static/images/top.png')

@server.route('/distribution')
def distribution():
    return 'Тут будет distribution'
