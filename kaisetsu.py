import os
import slack
import schedule
import time

# Set API token
bot_slack_token = 'xxx' # os.environ['SLACK_API_TOKEN']
user_slack_token = 'xxx'

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

    if schedule.every().day.at("16:05"):
        web_client.chat_postMessage( channel = channel_id, text = f"Hi <@{user_id}>!" )


    if '!kickme' in data.get( 'text', [] ):
        web_client.channels_kick( channel = channel_id, user = user_id )


while True:
    schedule.run_pending()
    time.sleep(1)

rtm_client.start()