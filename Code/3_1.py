ie# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:02:12 2018

@author: 11796
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)
