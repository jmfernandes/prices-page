import os
from flask import Flask, render_template, json

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#class Number(object):
#    def __init__(self):
#        self.aquire = urllib.urlopen("http://www.prices.datanab.net/us/gasoline_json")
#        self.unpacked = self.aquire.read()
#        self.data = json.loads(self.unpacked)

@app.route('/')
def index():
    return  render_template('prices.html')

@app.route('/us/fuel/gasoline', endpoint='gasoline')
def index():
    #req = urllib2.Request("http://www.prices.datanab.net/us/gasoline_json")
    json_file = open('templates/json/fuel/gasoline.json')
    data = json.load(json_file)
    json_file.close()
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
    #data = jsonify(value=3.492,units="dollars/gallon",name="Average Price of Gasoline in United States",citation="http://www.eia.gov/petroleum/gasdiesel/")
    #unpacked = aquire.read()
    #data = ast.literal_eval(unpacked)
    #opener = urllib2.build_opener()
    #results = opener.open(aquire)
    #final = results.read()
    #hey = urllib2.urlopen(aquire)
    return render_template('../../Constants/templates/webpage.html',data=data)

@app.route('/us/grocery/flour', endpoint='flour')
def index():
    json_file = open('templates/json/fuel/gasoline.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('grocery/flour.html',data=data)

@app.route('/us/fuel/gasoline_json', endpoint='gasoline_json')
def index():
    return render_template('json/fuel/gasoline.json')
           
@app.route('/us/grocery/flour_json', endpoint='flour_json')
def index():
    return render_template('json/grocery/flour.json')

#app.debug = True
#app.run()
#exit()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)