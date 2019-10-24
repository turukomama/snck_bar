import os
import slack

import random

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