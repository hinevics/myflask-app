from flask import Flask, render_template
import mtop
server = Flask(__name__)

@server.route('/')
def start():
    return render_template('index.html')

@server.route('/top')
def top():
    mtop.top_plot()
    return render_template('top.html')

@server.route('/distribution')
def distribution():
    return 'Тут будет distribution'

def main():
    server.run()

if __name__ == "__main__":
    main()