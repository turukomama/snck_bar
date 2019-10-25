import os
import slack

import random

#oshaberi つる子ママと発言すると結果を返す
@slack.RTMClient.run_on(event='message')
def oshaberi(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    # textはreplyなどには含まれないので、subtypeがなし=親メッセージかを確認する
    if 'subtype' not in data and 'つる子ママ' in data['text']:
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
            '注文は決まったの？' ,
            '・・・・・(無視)' ,
            'やっぱり福山雅治よねぇ～' ,
            '飲み足りないから飲んでんの～♪' ,
            '最近色気づいてきた？' 
            ]
        num = random.randint( 0, len( oshaberies ) - 1 )
        result = oshaberies[ num ]
   
        web_client.chat_postMessage(
            channel=channel_id,
            text = result,
            thread_ts=thread_ts
        )
#############################################################################