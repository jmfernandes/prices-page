import json
import urllib
aquire = urllib.urlopen("http://www.constants.datanab.net/physics/planck_constant_json")
unpacked = aquire.read()
data = json.loads(unpacked)

print data["value"]



exit()
import json

json_file = open('templates/json/gasoline.json')
data = json.load(json_file)
json_file.close()

print data