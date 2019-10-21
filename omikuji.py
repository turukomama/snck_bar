import os
import slack
import random

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
        num = random.randint(0, 2)
        if num == 0:
            kichi = "大吉"
        elif num == 1:
            kichi = "吉"
        elif num == 2:
            kichi = "凶"
        # thread_tsを設定することでスレッドでのリプライになる
        web_client.chat_postMessage(
            channel=channel_id,
            text=kichi,
            thread_ts=thread_ts
        )
slack_token = os.environ["SLACK_API_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()