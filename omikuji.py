import os
import slack

import random

#omikuji 占ってくださいと発言すると結果を返す
@slack.RTMClient.run_on(event='message')
def fortune(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    # textはreplyなどには含まれないので、subtypeがなし=親メッセージかを確認する
    if 'subtype' not in data and '占ってください' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        fortunes = [ '今日の鳥類は！「鶴」よ！ラッキープレイスは「会社」よ。',
         '今日の鳥類は！「インコ」よ！ラッキープレイスは「自宅」よ。',
          '今日の鳥類は！「カラス」よ！ラッキープレイスは「ごみ捨て場」よ。',
           '今日の鳥類は！「フクロウ」よ！ラッキープレイスは「樹海」よ。',
            '今日の鳥類は！「ペンギン」よ！ラッキープレイスは「海」よ。' ,
            '今日の鳥類は！「ドードー鳥」よ！ラッキープレイスは「マダガスカル」よ。' ,
            '今日の鳥類は！「不死鳥」よ！ラッキープレイスは「火山」よ。' ,
            '今日の鳥類は！「フラミンゴ」よ！ラッキープレイスは「二丁目」よ。' ,
            '今日の鳥類は！「ククルカン」よ！ラッキープレイスは「チチェン・イッツァ」よ。' ,
            '今日の鳥類は！「八咫烏」よ！ラッキープレイスは「サッカー場」よ。'
            ]
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

#omikuji お酒と発言すると結果を返す

@slack.RTMClient.run_on(event='message')
def alcohol(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    # textはreplyなどには含まれないので、subtypeがなし=親メッセージかを確認する
    if 'subtype' not in data and 'お酒' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        alcohols = [ '今日のおすすめはビールよ',
                    '今日のおすすめはウィスキーよ',
                    '今日のおすすめは赤ワインよ',
                    '今日のおすすめは白ワインよ',
                    '今日のおすすめは一刻者よ',
                    '今のおすすめは水道水よ。アンタ飲みすぎよ！',
                    '今日のおすすめはカシスオレンジよ',
                    '今日のおすすめは鏡月よ',
                    '今日のおすすめは魔王よ',
                    '今日のおすすめは白鶴よ',
                    '今日のおすすめはスピリタスよ',
                    '今日のおすすめはドンペリニヨンよ',
            ]
        num = random.randint( 0, len( alcohols ) - 1 )
        result = alcohols[ num ]
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
#############################################################################