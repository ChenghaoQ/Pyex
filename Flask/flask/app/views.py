from flask import render_template
from app import app
@app.route('/')
@app.route('/index')

def index():
#1        return "Hello world!"
        user={'nickname':'Miguel'}
        return render_template("index.html", user = user) 

