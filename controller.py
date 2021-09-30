# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, redirect
from werkzeug.utils import secure_filename
from flask import send_file
from datetime import date
from registerModel import *
from fetchModel import *

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


@app.route('/fetch', methods=['GET'])
def fetch():
    today = date.today()
    # YY/mm/dd
    dt = today.strftime("%Y-%m-%d")
    response = jsonify(fetchMovie(dt))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/data/photo/<path:path>")
def get_image(path):
    filename = 'data/photo/'+path+'.jpg'
    return send_file(filename, mimetype='image/jpg')


# driver function
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
