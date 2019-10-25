import os
import slack
import requests

from bs4 import BeautifulSoup

#　ニュース取得
def is_today_news():	
    r = requests.get("https://news.yahoo.co.jp/")
	
    soup = BeautifulSoup(r.text, "lxml")

    for b in soup.findAll('ul', {'class':'topicsList_main'}):
        news_list = b.find('a').get('href')  
        print(news_list)

        return news_list


    # 1.＠ニュース
    if '@ニュース' in data.get( 'text', [] ):
        # ２．ニュース情報を取得する
        is_news = is_today_news()
        # ３．今日のニュースをPOST
        web_client.chat_postMessage( channel = channel_id, text = is_news )


