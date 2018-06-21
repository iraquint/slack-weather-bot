import urllib.request
import json
import datetime

# Alexandria, VA

#city = input("Enter a city to check the weather: ")

weather_contents = urllib.request.urlopen("https://api.darksky.net/forecast/64127b8583a0e23fd8cf0aad56df2de3/38.820450,-77.050552?exclude=[minutely,daily,flags]/").read()
weather_json = json.loads(weather_contents.decode('utf-8'))

currently = weather_json['currently']
currently_summary = currently['summary']

print("\n\n\n--------- Currently Summary --------- " )

print("Hello! The current weather is:", currently_summary)
print("It's currently", int(currently['temperature']), "degrees, ( which feels like",
int(currently['apparentTemperature']),")")
#print(currently)
#print(currently_summary)
# print(
#     datetime.datetime.fromtimestamp(
#         currently['time']
#     ).strftime('%Y-%m-%d %H:%M:%S'))



hourly = weather_json['hourly']
hourly_summary = hourly['summary']

print("\n\n\n--------- Hourly Summary --------- ")
print("Hourly summary:", hourly_summary)

hourly_data = hourly['data']
next_12_hours = hourly_data[:12]

temp_low = 2500
temp_high = -1000

for hour in next_12_hours:
	if hour['temperature'] > temp_high:
		temp_high = hour['temperature']
	if hour['temperature'] < temp_low:
		temp_low = hour['temperature']

print("Over the next 12 hours, we'll see a high of", temp_high, "and a low of", temp_low)