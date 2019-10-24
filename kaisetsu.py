import os
import slack
import schedule
import time

# Set API token
bot_slack_token = 'xoxb-701987401137-800193405248-QSO0kAlWZjshxuEfmsCKFrsa' # os.environ['SLACK_API_TOKEN']
user_slack_token = 'xoxp-701987401137-776207167766-802402565478-79ad8d31854e626277f1e564edd5d90d'

# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

#
# Declare event hook methods
#

# on user has joined channel
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
    
    if '!kickme' in data.get( 'text', [] ):
        web_client.channels_kick( channel = channel_id, user = user_id )

def job():
    print("いらっしゃい")


schedule.every().day.at("10:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

rtm_client.start()