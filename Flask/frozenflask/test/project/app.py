'''from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__) #??????
app.config.from_pyfile('settings.py')  #为什么要这样导入设置
pages = FlatPages(app)
freezer = Freezer(app)
from .views import *

#this is where the Flask app,pages and freezer instances live'''
