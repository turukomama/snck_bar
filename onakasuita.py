import os
import slack
import random

client = slack.WebClient(token='xoxb-')

def choice_food():
    dir_path = 'C:\\Users\\a.watanabe\\Desktop\\workspace2\\food'
    # フォルダ内のファイル・フォルダリストを取得
    foodfiles = os.listdir( dir_path )
#    print(foodfiles)
    # ファイル・フォルダリストからファイル名だけを抜き出し
    foodfiles_file = [f for f in foodfiles if os.path.isfile(os.path.join( dir_path, f ) )]
#    print(foodfiles_file)
    # ファイル名リストからランダムに一つ取得
    postfile = random.choice(foodfiles_file) 
#    print(postfile)
    # ファイル名とフォルダ名を結合（フルパス作成）
    fullpath = os.path.join(dir_path,postfile)
    # フルパスを返却
    return fullpath

#print( choice_food() )

response = client.files_upload(
    channels = '#tsuruko_bar',
    file = choice_food()
    )
assert response["ok"]