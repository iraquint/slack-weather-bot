import urllib.request
import json
import datetime
import requests
import variables
import os

# Dark Sky API
# Coordinates are Alexandria, VA --> (38.820450,-77.050552)

weather_contents = urllib.request.urlopen("https://api.darksky.net/forecast/" + os.environ["DARKSKY_KEY"]+ "/38.820450,-77.050552?exclude=[minutely,daily,flags]/").read()
weather_json = json.loads(weather_contents.decode('utf-8'))

# " --------- Currently Summary --------- " )

currently = weather_json['currently']

currentlyString = "`Current weather:` " + currently['summary'] + ". It's currently " + str(currently['temperature']) + " degrees, ( which feels like " + str(currently['apparentTemperature']) + " )"

# print(datetime.datetime.fromtimestamp(currently['time']).strftime('%Y-%m-%d %H:%M:%S'))

# " --------- Hourly Summary --------- "

hourly = weather_json['hourly']

hourlyString = "`Daily Forecast:` " + hourly['summary'] 

hourly_data = hourly['data']
next_12_hours = hourly_data[:12]

# Determine temp. highs and lows

temp_low = float('Inf'); temp_high = -float('Inf')

for hour in next_12_hours:
	if hour['temperature'] > temp_high:
		temp_high = hour['temperature']
	if hour['temperature'] < temp_low:
		temp_low = hour['temperature']

tempString = "Over the next 12 hours, we'll see a high of `" + str(temp_high) + "` degrees and a low of `" + str(temp_low) + "` degrees"

# Make request to slack bot
r1 = requests.post("https://hooks.slack.com/services/" + os.environ["SLACK_KEY"], json={"text": currentlyString})
r2 = requests.post("https://hooks.slack.com/services/" + os.environ["SLACK_KEY"], json={"text": hourlyString})
r3 = requests.post("https://hooks.slack.com/services/" + os.environ["SLACK_KEY"], json={"text": tempString})

