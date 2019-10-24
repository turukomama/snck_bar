import os
import slack
import requests

# Set API token
bot_slack_token = '' # os.environ['SLACK_API_TOKEN']
user_slack_token = ''

# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

#
# Declare event hook methods
#

#天気
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
api_data = requests.get(url).json()
print(api_data['title'])
for weather in api_data['forecasts']:
      weather_date = weather['dateLabel']
      weather_forecasts = weather['telop']
     
      if weather_date == "今日" and "雨" in weather_forecasts:
            i = print("雨です")

      else:
            print(" ")

# on user has joined a channel
@slack.RTMClient.run_on( event = 'member_joined_channel' )
def on_member_joined_channel( **payload ):
    data = payload['data']
    
    channel_id = data[ 'channel' ]
    
    # for debug
    print( data )
    
    web_client.chat_postMessage( channel = channel_id, text = "Welcome to my channel!" )

# on user has sent a message
@slack.RTMClient.run_on( event = 'message' )
def on_message( **payload ):
    data = payload[ 'data' ]
    
    # for debug
    print( data )
    
    if 'subtype' in data:
        return

    channel_id = data[ 'channel' ]
    user_id = data[ 'user' ]
    
    if 'Hello' in data.get( 'text', [] ):
        web_client.chat_postMessage( channel = channel_id, text = f"Hi <@{user_id}>!" )

    if '雨降る？' in data.get( 'text', [] ):
        web_client.chat_postMessage( channel = channel_id, text = i )

    if '!kickme' in data.get( 'text', [] ):
        web_client.channels_kick( channel = channel_id, user = user_id )


            
