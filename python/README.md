# tanalisp/python

型システムとか大変そうだったので  
とりあえず python で概形だけでも実装しちゃおうと思いました。  

## info

virtualenv でパッケージ管理してます。`scripts/venv.bash` で  
そのへんは自動化してます。

テストフレームワークは `unittest` を採用しました。  
`scripts/unittest.bash`で勝手に走る。

# attention

`'` は未実装  
`#t`, `#f` はプリミティブになっていない

# primitive operators

* `car`
* `cdr`
* `cond`
* `cons`
* `define`
* `eq?`
* `lambda`
* `load`
* `quote`

# built-in functions

* `add1`
* `sub1`

(足し算引き算とかは定義しろスタイル)
