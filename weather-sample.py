import requests

url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
api_data = requests.get(url).json()
print(api_data['title'])
for weather in api_data['forecasts']:
      weather_date = weather['dateLabel']
      weather_forecasts = weather['telop']
      print(weather_date + ':' + weather_forecasts)