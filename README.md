## Slackつる子ママBot  
 Python3.  
 slackclient v2.2.1.  
### 機能一覧  
#### 1.チャンネルに常駐してスナックを開店  
営業時間は18:00~25:00  
開店時(18:00)にひとことをPOST「いらっしゃい」「今日もお疲れ様」など  
営業時間外は無反応  
#### 2.おしゃべり機能  
「!つる子ママ」の発言に対して返答してくれる機能  
「何飲むの？」、「ご無沙汰ねぇ」など  
#### 3.チャンネル追い出し機能  
「年齢」を含む発言をすると無言でチャンネルを追い出される  
#### 4.おすすめのお酒を教えてくれる機能  
「!お酒」の発言に対してランダムにおすすめのお酒を返信(提供)  
#### 5.鳥占い機能  
「!占ってください」の発言に対して今日の鳥類とラッキープレイスを返信  
#### 6.今日のニュースを教えてくれる機能  
「!ニュース」の発言に対してその日のニュースのURLを返す  
#### 7.傘が必要か教えてくれる機能  
「!雨降る？」の発言に対してその日の予報に雨が含まれていれば  
「雨が降りそうよ、傘持ってるの？」と返す  
#### 8.おなかすいた機能  
 「!おなかすいた」と発言すると食べ物の画像のみを返す  
#### 9.メニュー機能  
18:00にBotが反応する単語を一覧にしてPOST  
### Slack_bot_api_tokenの取得  
二種類のAPI tokenが必要です  
https://api.slack.com/apps  
### PythonへのGithubのimport   
$ git clone https://github.com/turukomama/snck_bar  
### SlackClientのimport  
`$ cd snck_bar`  
`$ py -m pip install slackclient`    
### settingにAPI tokenをセットする
`$ cp setting.turuko{.example,}`   
`$ vim setting.turuko`  


