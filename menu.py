import os
import slack
import settings

bot_slack_token = settings.xoxb_token
user_slack_token = settings.xoxp_token

rtm_client = slack.RTMClient( token = bot_slack_token )
web_client = slack.WebClient( token = user_slack_token )

# # menu_list = [
# #     # "ー今日のおすすめよ♪\nー１.おすすめのドリンク（「!お酒」）\n2.ママの手料理(「!おなかすいた」）\n3.ママの手料理(「!占ってください」))"
#     ]

web_client.chat_postMessage( channel = "tsuruko_bar", text = "Hello" )