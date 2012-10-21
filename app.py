import os
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('prices.html')

@app.route('/US/gasoline', endpoint='gasoline')
def hello():
    dict = {'value': 3.819, 'units': 'dollars/gallon', 'citation': 'http://www.eia.gov/petroleum/gasdiesel/','name': 'Average Price of Gasoline in United States'};
    data = json.dumps(dict)
    return data

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)