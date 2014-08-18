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
    json_file = open('templates/json/fuel/gasoline.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/goods/white_sugar', endpoint='white_sugar')
def index():
    json_file = open('templates/json/goods/white_sugar.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/housing/housing', endpoint='housing')
def index():
    json_file = open('templates/json/housing/housing.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

#Cereal

@app.route('/us/grocery/flour', endpoint='flour')
def index():
    json_file = open('templates/json/grocery/flour.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/bread_white', endpoint='bread_white')
def index():
    json_file = open('templates/json/grocery/bread_white.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/bread_whole_wheat', endpoint='bread_whole_wheat')
def index():
    json_file = open('templates/json/grocery/bread_whole_wheat.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/cookies_chocolate_chip', endpoint='cookies_chocolate_chip')
def index():
    json_file = open('templates/json/grocery/cookies_chocolate_chip.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/rice_white_long', endpoint='rice_white_long')
def index():
    json_file = open('templates/json/grocery/rice_white_long.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/spaghetti', endpoint='spaghetti')
def index():
    json_file = open('templates/json/grocery/spaghetti.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

"""JSON Data"""

@app.route('/us/fuel/gasoline_json', endpoint='gasoline_json')
def index():
    return render_template('json/fuel/gasoline.json')

@app.route('/us/goods/white_sugar_json', endpoint='white_sugar_json')
def index():
    return render_template('json/goods/white_sugar.json')

@app.route('/us/housing/housing_json', endpoint='housing_json')
def index():
    return render_template('json/housing/housing.json')

#CEREAL

@app.route('/us/grocery/flour_json', endpoint='flour_json')
def index():
    return render_template('json/grocery/flour.json')

@app.route('/us/grocery/bread_white_json', endpoint='bread_white_json')
def index():
    return render_template('json/grocery/bread_white.json')

@app.route('/us/grocery/bread_whole_wheat_json', endpoint='bread_whole_wheat_json')
def index():
    return render_template('json/grocery/bread_whole_wheat.json')

@app.route('/us/grocery/cookies_chocolate_chip_json', endpoint='cookies_chocolate_chip_json')
def index():
    return render_template('json/grocery/cookies_chocolate_chip.json')

@app.route('/us/grocery/rice_white_long_json', endpoint='rice_white_long_json')
def index():
    return render_template('json/grocery/rice_white_long.json')

@app.route('/us/grocery/spaghetti_json', endpoint='spaghetti_json')
def index():
    return render_template('json/grocery/spaghetti.json')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)