import os
import json
import urllib
import ast
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('prices.html')

@app.route('/us/gasoline', endpoint='gasoline')
def hello():
    menu = ["one","two","three"]
    return menu

@app.route('/us/gasoline_json', endpoint='gasoline_json')
def index():
    return  render_template('json/gasoline.json')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)