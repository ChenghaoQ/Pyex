from app import app
from flask import render_template,url_for
@app.route('/')
#@app.route('/index')
def index():
        maincss=url_for('static',filename='css/main.css')
        return render_template('index.html',maincss=maincss)
