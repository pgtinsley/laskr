
import glob

from random import choice

from flask import Flask, request, render_template, url_for

app = Flask(__name__)

fnames = glob.glob('./static/iris_images/*')
# print(fnames)

@app.route("/")
def index():
    fname = choice(fnames)
    return render_template("index.html", fname=fname)