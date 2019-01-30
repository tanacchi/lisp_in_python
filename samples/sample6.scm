; もうひとつの Scheme 入門より
; http://www.shido.info/lisp/idx_scm.htmli
; 3.2.2 list 式
; ２つ以上の引数からリストを作成する

(cons 1 (cons 2 (cons 3 '())))  ; 下の式と等価
(list 1 2 3)  ; => (1 2 3)

(list 3 (cons 1 2) 4)  ; => (3 (1 . 2) 4)
(cons #\a (list 3 "hello"))  ; => (#\a 3 "hello")
(list (cons 0 '()) (list 2 3) 4)  ; => ((0) (2 3) 4)
