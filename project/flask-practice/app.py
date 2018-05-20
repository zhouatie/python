# coding:utf8
import os
from flask import Flask, render_template, request, session
from werkzeug import secure_filename
UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return "<h1 style='color:red'>hello world</h1>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('./hello.html', name=name)

@app.route('/file', methods=['POST'])
def file():
    fileObj = request.files['file']
    filename = secure_filename(fileObj.filename)
    fileObj.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return '上传成功'


if __name__ == "__main__":
    app.run(debug=True)
