import os
import json
import urllib
import ast
from flask import Flask
from flask import render_template

app = Flask(__name__)

def numbers():
    aquire = urllib.urlopen("http://www.prices.datanab.net/us/gasoline_json")
    unpacked = aquire.read()
    data = ast.literal_eval(unpacked)
    data2 = json.dumps(data)
    return data2

@app.route('/')
def index():
    return  render_template('prices.html')

@app.route('/us/gasoline', endpoint='gasoline')
def hello():
    data3 = numbers()
    return data3

@app.route('/us/gasoline_json', endpoint='gasoline_json')
def index():
    return  render_template('json/gasoline.json')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)