import os
import slack
import requests
import random
import datetime
import settings

from bs4 import BeautifulSoup

# Set API token
bot_slack_token = settings.xoxb_token
user_slack_token = settings.xoxp_token

# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

# Operating time
open_time = **
close_time = *

# Get current time
def Current_time():
    now = datetime.datetime.now()
    hour_time = now.hour
    return hour_time


# now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
# close = datetime(now.year, now.month, now.day, **, 0, 0)
# diff = close - now

#
# Declare event hook methods
#


# Get Weather
def Download_weather():
        url = 'Web_URL'
        api_data = requests.get(url).json()
        print(api_data['title'])
        for weather in api_data['forecasts']:
            weather_date = weather['dateLabel']
            weather_forecasts = weather['telop']
            
            if weather_date == "TEXT" and "TEXT" in weather_forecasts:
                return True
            else:
                return False


#　Get News
def Download_news():	
    r = requests.get("Web_URL")
    print(r)
    soup = BeautifulSoup(r.text, "lxml")
    print(soup)
    for b in soup.findAll('ul', {'class':'topicsList_main'}):
        news_list = b.find('a').get('href')  
        print(news_list)

        return news_list


# random1 list
def random1():
        random1_list = [
            'TEXT',
            'TEXT'
            ]
        num = random.randint( 0, len( random1_list ) - 1 )
        result = random1_list[ num ]
        return result


# random2 list
def random2():
        random1_list = [
            'TEXT',
            'TEXT'
            ]
        num = random.randint( 0, len( random1_list ) - 1 )
        result = random1_list[ num ]
        return result


# random3 list
def random3():
        random3_list = [
            'TEXT',
            'TEXT'
            ]
        num = random.randint( 0, len( random3_list ) - 1 )
        result = random3_list[ num ]
        return result


# on user has sent a message
@slack.RTMClient.run_on( event = 'message' )
def on_message( **payload ):
    data = payload[ 'data' ]
    
    # for debug
    print( data )
    
    if 'subtype' in data:
        return

    user_id = data[ 'user' ]
    
    # １．What's the chance of rain today?
    if '!TEXT' in data.get( 'text', [] ):
        # ２．Get Weather
        is_rain = Download_weather()
        # 2. Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # ３．I wonder if it will rain today?
            if( is_rain ):
                # ４．３．It looks like rain
                msg_weather1 = "TEXT"
                web_client.chat_postMessage( channel = "channel_name", text = msg_weather1 )
            else:
                msg_weather2 ="TEXT"
                web_client.chat_postMessage( channel = "channel_name", text = msg_weather2 )

    # 1.Get News
    if  '!TEXT' in data.get( 'text', [] ):
        # 2. Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
        # 3．Get News
            dl_news = Download_news()
            # 4．Post information
            web_client.chat_postMessage( channel = "channel_name", text = "TEXT" )
            web_client.chat_postMessage( channel = "channel_name", text = dl_news )
   
    # 1.random1
    if '!TEXT' in data.get( 'text', [] ):
        # 2.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 3.draw a fortune slip
            tel_random1 = random1()
            # 4.Results
            web_client.chat_postMessage( channel = "channel_name", text = tel_random1 )

    # 1.random2
    if '!TEXT' in data.get( 'text', [] ):    
        # 2.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 3.draw a fortune slip
            rm_random2 = random2()
            # 4.Results
            web_client.chat_postMessage( channel = "channel_name", text = rm_random2 )

    # 1.random3
    if '!TEXT' in data.get( 'text', [] ):  
        # 2.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 2.draw a fortune slip
            talking_to_random3 = random3()
            # 3.Results
            web_client.chat_postMessage( channel = "channel_name", text = talking_to_random3 )


    #Removes a user from a channel
    if 'TEXT' in data.get( 'text', [] ):
        # 1.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 2. Removes a user from a channel
            web_client.channels_kick( channel = "channel_name", user = user_id )


rtm_client.start()