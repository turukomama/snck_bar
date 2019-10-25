import os
import slack

client = slack.WebClient(token=os.environ['xoxb-701987401137-792451981510-VUsMTOixCXc9xs0P6BoZnjO3'])

response = client.chat_postMessage(
    channel='#201910_test',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"