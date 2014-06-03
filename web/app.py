__author__ = 'jervyshi'
import os

import fileUtil

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

ALLOWED_EXTENSIONS = set(['zip', 'pdf'])
UPLOAD_FOLDER = '/tmp/verify/'
WORK_FOLDER = '/tmp/verify_work/'

app = Flask(__name__)
#app.config.from_envvar('APP_SETTINGS', silent=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # print app.config['UPLOAD_FOLDER']
    f = fileUtil.get_all_file(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=f)


@app.route('/upload', methods=['GET', 'POST'])
def upload():

    pass

if __name__ == '__main__':
    app.run(debug=True)