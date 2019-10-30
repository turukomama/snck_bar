import os
import slack

client = slack.WebClient(token='xoxb-')

response = client.files_upload(
    channels='#tsuruko_bar',
    file="takoyaki.jpg")
assert response["ok"]