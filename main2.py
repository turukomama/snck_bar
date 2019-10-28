import os
import slack
import requests
import random
import datetime

from bs4 import BeautifulSoup

# Set API token
bot_slack_token = "xoxb"
user_slack_token = "xoxp"


# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

#
# Declare event hook methods
#
now = datetime.datetime.now()
hour_time = now.hour
# now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
# close = datetime(now.year, now.month, now.day, 18, 0, 0)
# diff = close - now

# 天気機能
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


#　ニュース機能
def is_today_news():	
    r = requests.get("https://news.yahoo.co.jp/")
	
    soup = BeautifulSoup(r.text, "lxml")

    for b in soup.findAll('ul', {'class':'topicsList_main'}):
        news_list = b.find('a').get('href')  
        print(news_list)

        return news_list


# 鳥おみくじ機能
def is_today_fortunes():
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
        return result
        # if num == 0:
        #     kichi = "大吉"
        # elif num == 1:
        #     kichi = "吉"
        # elif num == 2:
        #     kichi = "凶"
        # thread_tsを設定することでスレッドでのリプライになる


# お酒おみくじ機能
def is_today_alcohols():
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
        return result
        # if num == 0:
        #     kichi = "大吉"
        # elif num == 1:
        #     kichi = "吉"
        # elif num == 2:
        #     kichi = "凶"
        # thread_tsを設定することでスレッドでのリプライになる


# おしゃべり機能
def oshaberi():
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
        return result


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
    if '!雨降る?' in data.get( 'text', [] ):
        # ２．天気情報を取得する
        is_rain = is_today_rainy()
        # ３．今日が雨か？
        if( is_rain ):
            # ４．３．が雨ならメッセージ
            msg_weather1 = "雨が降りそうよ、傘持ってるの？"
            web_client.chat_postMessage( channel = channel_id, text = msg_weather1 )
        else:
            msg_weather2 ="大丈夫そうよ"
            web_client.chat_postMessage( channel = channel_id, text = msg_weather2 )

    # 1.ニュース
    if  '!ニュース' in data.get( 'text', [] ) and 18 <= hour_time <= 24: 
        # ２．ニュース情報を取得する
        is_news = is_today_news()
        # ３．今日のニュースをPOST
        web_client.chat_postMessage( channel = channel_id, text = "今日こんな事があったわよ" )
        web_client.chat_postMessage( channel = channel_id, text = is_news )
   

    # 1.鳥おみくじ
    if '!占ってください' in data.get( 'text', [] ) and 18 <= hour_time <= 24:
        # 2.おみくじ結果を取得
        is_fortunes = is_today_fortunes()
        # 3.おみくじ結果をPOST
        web_client.chat_postMessage( channel = channel_id, text = is_fortunes )

    # 1.お酒おみくじ
    if '!お酒' in data.get( 'text', [] ) and 18 <= hour_time <= 24:    
        # 2.おみくじ結果を取得
        is_alcohols = is_today_alcohols()
        # 3.おみくじ結果をPOST
        web_client.chat_postMessage( channel = channel_id, text = is_alcohols )

    # 1.おしゃべり
    if '!つる子ママ' in data.get( 'text', [] ) and 18 <= hour_time <= 24:  
        # 2.おみくじ結果を取得
        is_oshaberi = oshaberi()
        # 3.おみくじ結果をPOST
        web_client.chat_postMessage( channel = channel_id, text = is_oshaberi )


    #キック機能
    if '年齢' in data.get( 'text', [] ) and 18 <= hour_time <= 24:
        web_client.channels_kick( channel = channel_id, user = user_id )

rtm_client.start()