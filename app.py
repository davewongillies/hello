import os

import flask_bootstrap

from flask import Flask, render_template, request

app = Flask(__name__)
flask_bootstrap.Bootstrap(app)


@app.route('/')
def index():
    data = request.environ
    environ = os.environ

    return render_template('index.html', data=data, environ=environ)


if __name__ == '__main__':
    app.run()
