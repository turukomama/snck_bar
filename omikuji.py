import os
import slack

import random

#omikuji fortuneと発言すると結果を返す########################################

@slack.RTMClient.run_on(event='message')
def fortune(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    # textはreplyなどには含まれないので、subtypeがなし=親メッセージかを確認する
    if 'subtype' not in data and 'fortune' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        fortunes = [ '大吉', '吉', '凶', '中吉', '小吉' ]
        num = random.randint( 0, len( fortunes ) - 1 )
        result = fortunes[ num ]
        # if num == 0:
        #     kichi = "大吉"
        # elif num == 1:
        #     kichi = "吉"
        # elif num == 2:
        #     kichi = "凶"
        # thread_tsを設定することでスレッドでのリプライになる
        web_client.chat_postMessage(
            channel=channel_id,
            text = result,
            thread_ts=thread_ts
        )
###############################################################################
