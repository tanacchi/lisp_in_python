; もうひとつの Scheme 入門より
; http://www.shido.info/lisp/idx_scm.htmli
; 3.4.2 cdr 式
; リストの cdr 部を取り出す

(cdr '(0))  ; => ()
(cdr '((1 2 3) (4 5 6)))  ; => (4 5 6)
(cdr '(1 2 3 . 4))        ; => (2 3 . 4)
(cdr (cons 3 (cons 2 (cons 1 '()))))  ; => (2 1)
