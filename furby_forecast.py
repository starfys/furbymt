import requests
import json

# KEY = 929dc6ca2a059b1d

r = requests.get('http://api.wunderground.com/api/929dc6ca2a059b1d/forecast/q/TN/Murfreesboro.json')
parsed_json = json.loads(r.text)
period_list = parsed_json['forecast']
forecasts = []

for period in parsed_json['forecast']['txt_forecast']['forecastday']:
	period_forecast = ("{}: {}".format(period['title'],period['fcttext']))
	forecasts.append(period_forecast)

def get_forecast(day):
	
	if day == '0':
		dayNum = 0
	elif day == '1':
		dayNum = 1
	elif day == '2':
		dayNum = 2
	elif day == '3':
		dayNum = 3
	elif day == '4':
		dayNum = 4
	elif day == '5':
		dayNum = 5
	else:
		dayNum = -1

	string = forecasts[dayNum]
	return string