import requests
import json
import re

# KEY = 929dc6ca2a059b1d

r = requests.get('http://api.wunderground.com/api/929dc6ca2a059b1d/forecast/q/TN/Murfreesboro.json')
parsed_json = json.loads(r.text)
period_list = parsed_json['forecast']
forecasts = []

for period in parsed_json['forecast']['txt_forecast']['forecastday']:
	period_forecast = ("{}: {}".format(period['title'],period['fcttext']))
	forecasts.append(period_forecast)

def get_forecast(day):
	
	string = forecasts[day]
	string = string.replace("mph", "miles per hour")
	string = string.replace(" NNE ", " norf norfeast ")
	string = string.replace(" NE ", " norfeast ")
	string = string.replace(" ENE ", " east norfeast ")
	string = string.replace(" ESE ", " east southeast ")
	string = string.replace(" SE ", " southeast ")
	string = string.replace(" SSE ", " south southeast ")
	string = string.replace(" SSW ", " south southwest ")
	string = string.replace(" SW ", " southwest ")
	string = string.replace(" WSW ", " west southwest ")
	string = string.replace(" WNW ", " west norf ")
	string = string.replace(" NW ", " norfwest ")
	string = string.replace(" NNW ", " norf norfwest ")

	return re.sub(r'([0-9]+)F', r'\1 fahrenheit', string)
