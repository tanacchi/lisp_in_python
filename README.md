# tanalisp

C++ および Python で  
Lisp インタプリタを実装する。

TDD を採用するつもり

## Product Specification
ひとまず簡単に作れそうなものに設定

### Primitives

Name | Description
--- | ---
`atom` | アトムかどうかの判定
`eq` | 2つのアトムが等しいかの判定
`car` | ペアの左値を取り出す
`cdr` | ペアの右値を取り出す
`cons` | 2要素からコンスセルを作る

### Special Forms

Name | Description
--- | ---
`cond` | 条件分岐
`define` | 変数の定義
`defun` | 関数の定義
`quote` | 引数を評価せずに返す
