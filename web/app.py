__author__ = 'jervyshi'
import os

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

ALLOWED_EXTENSIONS = set(['zip', 'pdf'])

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)


@app.route('/')
def index():
    # print app.config['UPLOAD_FOLDER']
    return render_template('index.html')


@app.route('/upload')
def upload():

    pass

if __name__ == '__main__':
    app.run(debug=True)