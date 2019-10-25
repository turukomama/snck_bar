import os
import slack
import settings
import requests
import random

from bs4 import BeautifulSoup

# Set API token
bot_slack_token = settings.xoxb_token
user_slack_token = settings.xoxp_token



# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

#
# Declare event hook methods
#
#天気
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

#　ニュース
def is_today_news():	
    r = requests.get("https://news.yahoo.co.jp/")
	
    soup = BeautifulSoup(r.text, "lxml")

    for b in soup.findAll('ul', {'class':'topicsList_main'}):
        news_list = b.find('a').get('href')  
        print(news_list)

        return news_list

# おみくじ
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



# on user has joined a channel
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
    
    # １．雨ふる？
    if '雨降る？' in data.get( 'text', [] ):
        # ２．天気情報を取得する
        is_rain = is_today_rainy()
        # ３．今日が雨か？
        if( is_rain ):
            # ４．３．が雨ならメッセージ
            msg = "雨が降りそうよ、傘持ってるの？"
            web_client.chat_postMessage( channel = channel_id, text = msg )

    # 1.＠ニュース
    if '@ニュース' in data.get( 'text', [] ):
        # ２．ニュース情報を取得する
        is_news = is_today_news()
        # ３．今日のニュースをPOST
        web_client.chat_postMessage( channel = channel_id, text = is_news )

    # おみくじ
    if 'subtype' not in data and '占ってください' in data['text']:
        # 2.おみくじ結果を取得
        is_fortunes = is_today_fortunes()
        # 3.おみくじ結果をPOST
        web_client.chat_postMessage( channel = channel_id, text = is_fortunes )


    if '年齢' in data.get( 'text', [] ):
        web_client.channels_kick( channel = channel_id, user = user_id )

rtm_client.start()