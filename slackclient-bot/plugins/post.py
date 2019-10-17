import os
import slack

client = slack.WebClient(token="xoxb-xxxxxxxxxxxxxxxxxxxxxxx")
response = client.chat_postMessage(
channel='#201910_test',
as_user=True,
text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"
