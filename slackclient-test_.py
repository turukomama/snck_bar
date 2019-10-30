import os
import slack
import datetime
import time
import threading

# Set API token
bot_slack_token = 'xoxb-' # os.environ['SLACK_API_TOKEN']
user_slack_token = 'xoxp-'

# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

def clock_timer():
    while True:
        print( datetime.datetime.now() )
        time.sleep( 0.5 )

clock_thread = threading.Thread( target = clock_timer )
clock_thread.daemon = True
clock_thread.start()

#
# Declare event hook methods
#

# on user has joined channel
@slack.RTMClient.run_on( event = 'member_joined_channel' )
def on_member_joined_channel( **payload ):
    data = payload['data']
    
    # for debug
    print( data )
    
    channel_id = data[ 'channel' ]
    
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

rtm_client.start()
