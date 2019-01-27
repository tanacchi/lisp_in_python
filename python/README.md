# tanalisp/python

型システムとか大変そうだったので  
とりあえず python で概形だけでも実装しちゃおうと思いました。  

## info

virtualenv でパッケージ管理してます。`scripts/venv.bash` で  
そのへんは自動化してます。

テストフレームワークは `unittest` を採用しました。  
`scripts/unittest.bash`で勝手に走る。

以下、各ソースの紹介

Script Name | Description
--- | ---
lisp01.py | 一番頭に優しいやつ。単に関数でリストを受け取り<br>先頭の文字を見て挙動を変える。そのうち消す。


