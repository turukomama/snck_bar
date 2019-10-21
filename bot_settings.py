import os
import slack

import random

# Set API token
bot_slack_token = 'xoxb-xxxxxxxxxxxxxxxx' # os.environ['SLACK_API_TOKEN']
user_slack_token = 'xoxp-xxxxxxxxxxxxxxxxxxxxxxxxx'

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
    
    # for debug
    print( data )
    
    channel_id = data[ 'channel' ]
    
    web_client.chat_postMessage( channel = channel_id, text = "Welcome to my channel!" )

# post　message
client = slack.WebClient( token= "xoxb-701987401137-787500056018-V8FtjryUaTBoh5l27ZVzO5TB" )
response = client.chat_postMessage(
channel='#201910_test',
as_user=True,
text="Hi!")

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
    
rtm_client.start()