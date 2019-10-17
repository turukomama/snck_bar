# coding: utf-8
from slackbot.bot import respond_to  # メンションで反応
from slackbot.bot import listen_to  # チャンネル内発言で反応
from slackbot.bot import default_reply  # 該当する応答がない場合に反応
import os
import slack
# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           メンションでは反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する

@default_reply()
def default(message):
    message.reply("デフォルトの返答")

@listen_to("反応語句")
def listen(message):
    message.reply("返事")

@respond_to("反応語句")
def respod(message):
    message.reply("返事")