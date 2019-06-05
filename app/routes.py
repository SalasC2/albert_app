from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"