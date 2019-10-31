import os
import slack
import requests
import random
import datetime
import settings
import datetime
import time
import threading

from bs4 import BeautifulSoup
# Set API token
bot_slack_token = settings.xoxb_token
user_slack_token = settings.xoxp_token

# Set channel_id
channel_id = "channel"

# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

# Business hours
open_time = 00
close_time = 00

# Get time
def Current_time():
    now = datetime.datetime.now()
    hour_time = now.hour
    return hour_time

# now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
# close = datetime(now.year, now.month, now.day, 00, 0, 0)
# diff = close - now


#
# Declare event hook methods
#


# Menu display at 00:00
def clock_timer():
    while True:
        menu_list = "ーmenuー\
            　　　　　n1.TEXT(「!TEXT」)\
            　　　　　n2.TEXT(「!TEXT」)\
            　　　　　n3.TEXT(「!TEXT」)\
            　　　　　n4.TEXT(「!TEXT」)\
            　　　　　n5.TEXT(「!TEXT」)"

        #Get now time
        now_time = datetime.datetime.now().strftime("%H:%M:%S") 
        print(now_time)
        if now_time == ("00:00:00"):
            web_client.chat_postMessage( channel = channel_id, text = menu_list )
        
        elif now_time == ("00:00:00"):
            post_word = Post_today_word()
            web_client.chat_postMessage( channel = channel_id, text = post_word )

        time.sleep( 1 )

clock_thread = threading.Thread( target = clock_timer )
clock_thread.daemon = True
clock_thread.start()


# Post random word
def Post_today_word():
        word_list = [
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT'
            ]
        num = random.randint(0, len( word_list )- 1)
        result = word_list[ num ]
        return result


# Get Weather
def Download_weather():
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
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
    r = requests.get("https://news.yahoo.co.jp/")
    print(r)
    soup = BeautifulSoup(r.text, "lxml")
    print(soup)
    for b in soup.findAll('ul', {'class':'topicsList_main'}):
        news_list = b.find('a').get('href')  
        print(news_list)

        return news_list


# Bird fortune list
def Tell_fortunes():
        fortunes = [
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT'
            ]
        num = random.randint( 0, len( fortunes ) - 1 )
        result = fortunes[ num ]
        return result


# Alcohol fortune list
def Recommend_alcohols():
        alcohols = [
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT'
            ]
        num = random.randint( 0, len( alcohols ) - 1 )
        result = alcohols[ num ]
        return result

# Talking list
def Talk_to():
        talking_list = [
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT',
            'TEXT'
            ]
        num = random.randint( 0, len( talking_list ) - 1 )
        result = talking_list[ num ]
        return result


# food list
client = slack.WebClient(token='xoxb-')

def choice_file():
    dir_path = 'File'
    # Get a list of files and folders in a folder
    files = os.listdir( dir_path )
    # Extract only file names from file/folder list
    files_file = [f for f in files if os.path.isfile(os.path.join( dir_path, f ) )]
    # Get one randomly from the file name list
    postfile = random.choice(files_file) 
    # Full path creation
    fullpath = os.path.join(dir_path,postfile)
    # Return the full pathname
    return fullpath


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
        # 3. Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 4．I wonder if it will rain today?
            if( is_rain ):
            # 5．It looks like rain
                msg_weather1 = "TEXT"
                web_client.chat_postMessage( channel = channel_id, text = msg_weather1 )
            else:
                msg_weather2 ="TEXT"
                web_client.chat_postMessage( channel = channel_id, text = msg_weather2 )

    # 1.Get News
    if  '!TEXT' in data.get( 'text', [] ):
        # 2. Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 3．Get News
            dl_news = Download_news()
            # 4．Post information
            web_client.chat_postMessage( channel = channel_id, text = "TEXT" )
            web_client.chat_postMessage( channel = channel_id, text = dl_news )
   
    # 1.Bird fortune
    if '!TEXT' in data.get( 'text', [] ):
        # 2.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 3.draw a fortune slip
            tel_fortunes = Tell_fortunes()
            # 4.Results
            web_client.chat_postMessage( channel = channel_id, text = tel_fortunes )

    # 1.Alcohol fortune
    if '!TEXT' in data.get( 'text', [] ):    
        # 2.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 3.draw a fortune slip
            rm_alcohols = Recommend_alcohols()
            # 4.Results
            web_client.chat_postMessage( channel = channel_id, text = rm_alcohols )

    # 1.Talking
    if '!TEXT' in data.get( 'text', [] ):  
        # 2.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 2.draw a fortune slip
            talking_to = Talk_to()
            # 3.Results
            web_client.chat_postMessage( channel = channel_id, text = talking_to )

    # 1.Get food
    if  '!TEXT' in data.get( 'text', [] ):
        # 2. Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
        # 3.Results
           response = client.files_upload(
           channels = 'channel',
           file = choice_file())
           assert response["ok"]

    #Removes a user from a channel
    if 'TEXT' in data.get( 'text', [] ):
        # 1.Get time
        cr_time = Current_time()
        if open_time <= cr_time <= close_time:
            # 2. Removes a user from a channel
            web_client.channels_kick( channel = channel_id, user = user_id )

rtm_client.start()