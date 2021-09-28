# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, redirect
from admin import *

# creating a Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return "Happy Birthday API"


@app.route('/post', methods=['POST'])
def disp():
    if request.method == 'POST':
        # return redirect(url_for('index'))
        uid = request.form['uid']
        name = request.form['name']
        dob = request.form['dob']
        dpt = request.form['dpt']
        append(uid, name, dob, dpt)
        return redirect("http://127.0.0.1:5500/")


# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
