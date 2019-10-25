import os
import slack
import requests

# Set API token
bot_slack_token = 'xoxb-' # os.environ['SLACK_API_TOKEN']
user_slack_token = 'xoxp-'

# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

#天気を取得するメソッド
def is_today_rainy():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    api_data = requests.get(url).json()
    print(api_data['title'])
    for weather in api_data['forecasts']:
        weather_date = weather['dateLabel']
        weather_forecasts = weather['telop']
        
        if weather_date == "今日" and "雨" in weather_forecasts:
            return True
        else:
            return False

# on user has joined a channel
@slack.RTMClient.run_on( event = 'member_joined_channel' )
def on_member_joined_channel( **payload ):
    data = payload['data']
    
    channel_id = data[ 'channel' ]
    
    # for debug
    print( data )
    
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
    
    # １．雨ふる？
    if '雨降る？' in data.get( 'text', [] ):
        # ２．天気情報を取得する
        is_rain = is_today_rainy()
        # ３．今日が雨か？
        if( is_rain ):
            # ４．３．が雨ならメッセージ
            msg = "雨が降りそうよ、傘持ってるの？"
            web_client.chat_postMessage( channel = channel_id, text = msg )

rtm_client.start()