import os
import slack

client = slack.WebClient(token=os.environ['xoxb-701987401137-791866640677-piiWLISjoGMSBjFrq7g8bAax'])

response = client.chat_postMessage(
    channel='#test-kuramochi',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"