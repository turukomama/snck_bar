import os
import slack
import schedule
import time
import random

# Set API token
bot_slack_token = 'xoxb-701987401137-800193405248-ubIapSUX89g0gqcbdKelrEMQ' # os.environ['SLACK_API_TOKEN']
user_slack_token = 'xoxp-701987401137-776207167766-807008845600-4cf1afd575773bbe7cabdea85c3ed6ff'

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
    
#oshaberi ＠つる子ママと発言すると結果を返す
@slack.RTMClient.run_on(event='message')
def oshaberi(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    # textはreplyなどには含まれないので、subtypeがなし=親メッセージかを確認する
    if 'subtype' not in data and '@つる子ママ' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        oshaberies = [ '今忙しいのよ',
         'いい子で待ってなさい',
          'あら、いらっしゃい',
           '何飲むの？',
            '鶴は千年...あらヤダ！' ,
            'キエェェェェェ！！' ,
            'ご無沙汰ねぇ' ,
            '注文は決まったの？' 
            ]
        num = random.randint( 0, len( oshaberies ) - 1 )
        result = oshaberies[ num ]
        # if num == 0:
        #     kichi = "今忙しいのよ"
        # elif num == 1:
        #     kichi = "いい子で待ってなさい"
        # elif num == 2:
        #     kichi = "あら、いらっしゃい"
        # thread_tsを設定することでスレッドでのリプライになる
        web_client.chat_postMessage(
            channel=channel_id,
            text = result,
            thread_ts=thread_ts
        )

###############################################################################

rtm_client.start()