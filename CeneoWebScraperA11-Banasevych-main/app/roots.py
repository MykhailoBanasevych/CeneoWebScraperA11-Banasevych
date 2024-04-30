from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template("base_html")

@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'