__author__ = 'jervyshi'
import os

import fileUtil

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from werkzeug.utils import secure_filename
from verify_zip_file import verifyfile

ALLOWED_EXTENSIONS = set(['zip', 'war'])
UPLOAD_FOLDER = '/export/data/verify/upload/'
WORK_FOLDER = '/export/data/verify/work/'
LOG_FOLDER = '/export/data/verify/log/'
RESULT_FOLDER = '/export/data/verify/result/'

app = Flask(__name__)
#app.config.from_envvar('APP_SETTINGS', silent=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    f = fileUtil.get_all_file(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=f)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            file_name = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    return redirect(url_for('index'))


@app.route('/verify/<name>')
def verify(name):
    print name
    vf = verifyfile.VerifyFile(UPLOAD_FOLDER + name, WORK_FOLDER, 'config.ini', True)
    vf.walk()
    return jsonify(name=name)


@app.route('/detail/<name>')
def detail(name):
    print name
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)