# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, redirect
from werkzeug.utils import secure_filename
from admin import *

# creating a Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return "Happy Birthday API"


@app.route('/post', methods=['POST'])
def disp():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = "temp.jpg"
        f.save(secure_filename(f.filename))
        uid = request.form['uid']
        name = request.form['name']
        dob = request.form['dob']
        dpt = request.form['dpt']
        append(uid, name, dob, dpt)
        img(uid)
        return redirect("http://127.0.0.1:5500/")


# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
