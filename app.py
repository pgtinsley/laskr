
import glob

from random import choice

from flask import Flask, request, render_template, url_for

fapp = Flask(__name__)

fnames = glob.glob('./static/iris_images/*')

@fapp.route("/")
def index():
    fname = choice(fnames)
    return render_template("index.html", fname=fname)
    
if __name__ == "__main__":
    fapp.run(host='0.0.0.0')