import json

json_file = open('templates/json/gasoline.json')
data = json.load(json_file)
json_file.close()

print data