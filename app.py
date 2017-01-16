import os
from flask import Flask, render_template, json, request, redirect

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

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
    return render_template('prices.html')

"""Web pages"""

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





@app.route('/us/grocery/bacon', endpoint='bacon')
def index():
    json_file = open('templates/json/grocery/meat/bacon.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/beef_ground_chuck', endpoint='beef_ground_chuck')
def index():
    json_file = open('templates/json/grocery/meat/beef_ground_chuck.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/beef_ground_lean', endpoint='beef_ground_lean')
def index():
    json_file = open('templates/json/grocery/meat/beef_ground_lean.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/beef_ground', endpoint='beef_ground')
def index():
    json_file = open('templates/json/grocery/meat/beef_ground.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/bologna', endpoint='bologna')
def index():
    json_file = open('templates/json/grocery/meat/bologna.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/chicken_boneless', endpoint='chicken_boneless')
def index():
    json_file = open('templates/json/grocery/meat/chicken_boneless.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/chicken_breast', endpoint='chicken_breast')
def index():
    json_file = open('templates/json/grocery/meat/chicken_breast.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/chicken_legs', endpoint='chicken_legs')
def index():
    json_file = open('templates/json/grocery/meat/chicken_legs.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/chicken_whole', endpoint='chicken_whole')
def index():
    json_file = open('templates/json/grocery/meat/chicken_whole.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/chuck_roast', endpoint='chuck_roast')
def index():
    json_file = open('templates/json/grocery/meat/chuck_roast.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/ham', endpoint='ham')
def index():
    json_file = open('templates/json/grocery/meat/ham.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/pork_chop_boneless', endpoint='pork_chop_boneless')
def index():
    json_file = open('templates/json/grocery/meat/pork_chop_boneless.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/pork_chop_center_cut', endpoint='pork_chop_center_cut')
def index():
    json_file = open('templates/json/grocery/meat/pork_chop_center_cut.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/round_roast', endpoint='round_roast')
def index():
    json_file = open('templates/json/grocery/meat/round_roast.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/us/grocery/steak_sirloin', endpoint='steak_sirloin')
def index():
    json_file = open('templates/json/grocery/meat/steak_sirloin.json')
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

#meat

@app.route('/us/grocery/bacon_json', endpoint='bacon_json')
def index():
    return render_template('json/grocery/meat/bacon.json')

@app.route('/us/grocery/beef_ground_chuck_json', endpoint='beef_ground_chuck_json')
def index():
    return render_template('json/grocery/meat/beef_ground_chuck.json')

@app.route('/us/grocery/beef_ground_lean_json', endpoint='beef_ground_lean_json')
def index():
    return render_template('json/grocery/meat/beef_ground_lean.json')

@app.route('/us/grocery/beef_ground_json', endpoint='beef_ground_json')
def index():
    return render_template('json/grocery/meat/beef_ground.json')

@app.route('/us/grocery/bologna_json', endpoint='bologna_json')
def index():
    return render_template('json/grocery/meat/bologna.json')

@app.route('/us/grocery/chicken_boneless_json', endpoint='chicken_boneless_json')
def index():
    return render_template('json/grocery/meat/chicken_boneless.json')

@app.route('/us/grocery/chicken_breast_json', endpoint='chicken_breast_json')
def index():
    return render_template('json/grocery/meat/chicken_breast.json')

@app.route('/us/grocery/chicken_legs_json', endpoint='chicken_legs_json')
def index():
    return render_template('json/grocery/meat/chicken_legs.json')

@app.route('/us/grocery/chicken_whole_json', endpoint='chicken_whole_json')
def index():
    return render_template('json/grocery/meat/chicken_whole.json')

@app.route('/us/grocery/chuck_roast_json', endpoint='chuck_roast_json')
def index():
    return render_template('json/grocery/meat/chuck_roast.json')

@app.route('/us/grocery/ham_json', endpoint='ham_json')
def index():
    return render_template('json/grocery/meat/ham.json')

@app.route('/us/grocery/prok_chop_boneless_json', endpoint='prok_chop_boneless_json')
def index():
    return render_template('json/grocery/meat/prok_chop_boneless.json')

@app.route('/us/grocery/pork_chop_center_cut_json', endpoint='pork_chop_center_cut_json')
def index():
    return render_template('json/grocery/meat/pork_chop_center_cut.json')

@app.route('/us/grocery/round_roast_json', endpoint='round_roast_json')
def index():
    return render_template('json/grocery/meat/round_roast.json')

@app.route('/us/grocery/steak_sirloin_json', endpoint='steak_sirloin_json')
def index():
    return render_template('json/grocery/meat/steak_sirloin.json')



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.debug = False
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)