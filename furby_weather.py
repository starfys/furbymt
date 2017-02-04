# weather.py

import requests
import json

# KEY = 929dc6ca2a059b1d

r = requests.get('http://api.wunderground.com/api/929dc6ca2a059b1d/geolookup/conditions/q/TN/Murfreesboro.json')
parsed_json = json.loads(r.text)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']

string = ("Current temperature in {} is: {} fahrenheit.".format(location, temp_f))
return string

