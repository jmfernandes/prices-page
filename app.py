import os
#import json
import urllib2
import ast
from flask import Flask
from flask import render_template
from flask import json
#from google.appengine.api import urlfetch

app = Flask(__name__)

#class Number(object):
#    def __init__(self):
#        self.aquire = urllib.urlopen("http://www.prices.datanab.net/us/gasoline_json")
#        self.unpacked = self.aquire.read()
#        self.data = json.loads(self.unpacked)

@app.route('/')
def index():
    return  render_template('prices.html')

@app.route('/us/gasoline', endpoint='gasoline')
def index():
    req = urllib2.Request("http://www.prices.datanab.net/us/gasoline_json")
    #response = urllib2.urlopen(req)
    #data2 = response.read()
    #data = json.loads(data2)
    #logging.info('url%s' % url)
    #result = urlfetch.fetch(url)
    #jsondata = json.loads(result.content)
    #jsondata = json.load(urllib.urlopen(url))
    #aquire = urllib2.Request("http://www.prices.datanab.net/us/gasoline_json")
    #response = urllib2.urlopen(aquire)
    #the_page = aquire.read()
    #data = json.loads(the_page)
    #aquire2 = str(aquire)
    #unpacked = json.loads(aquire2)
    data = jsonify(value=3.492,units="dollars/gallon",name="Average Price of Gasoline in United States",citation="http://www.eia.gov/petroleum/gasdiesel/")
    dict = {
    "value": 3.492,
    "units": "dollars/gallon",
    "name": "Average Price of Gasoline in United States",
    "citation": "http://www.eia.gov/petroleum/gasdiesel/"
    }
    #unpacked = aquire.read()
    #data = ast.literal_eval(unpacked)
    #opener = urllib2.build_opener()
    #results = opener.open(aquire)
    #final = results.read()
    #hey = urllib2.urlopen(aquire)
    return render_template('gasoline.html',data=dict)

@app.route('/us/gasoline_json', endpoint='gasoline_json')
def index():
    return render_template('json/gasoline.json')

#app.debug = True
#app.run()
#exit()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)