; もうひとつの Scheme 入門より
; http://www.shido.info/lisp/idx_scm.htmli
; 3.4.1 car 式
; リストの car 部を取り出す

(car '(0))  ; => 0
(car '((1 2 3) (4 5 6)))  ; => (1 2 3)
(car '(1 2 3 . 4))        ; => 1
(car (cons 3 (cons 2 (cons 1 '()))))  ; => 3
