import os
import slack
import schedule
import time

# Set API token
# bot_slack_token = 'xoxb-xxxxxxxxxxx' user_slack_token ='xoxp-xxxxxxxxxxxxxxxx'
 # os.environ['SLACK_API_TOKEN']


# Create both rtm client and web client
rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

def job():
     web_client.chat_postMessage( channel = '# 201910_test', text = "閉店よ" )

schedule.every().day.at("1:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

rtm_client.start()