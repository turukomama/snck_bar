import schedule
import time
import slack
import os

client = slack.WebClient(token=os.environ['xoxp-701987401137-776207167766-802402565478-79ad8d31854e626277f1e564edd5d90d'])

response = client.chat_postMessage(
    channel='#201910_test',
    text="いらっしゃい")
assert response["ok"]
assert response["message"]["text"] == "いらっしゃい"

schedule.every().day.at("10:59").do(response)

while True:
    schedule.run_pending()
    time.sleep(1)