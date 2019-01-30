; もうひとつの Scheme 入門より
; http://www.shido.info/lisp/idx_scm.htmli
; 3.2.1 cons 式
; ２つの引数からコンスセルを作成する

(cons 1 2)  ; => (1 . 2)
(cons 3 (cons 1 2))  ; => (3 (1 . 2)) => (3 1 . 2)
(cons #\a (cons 3 "hello"))  ;=> (#\a 3 . "hello")
(cons (cons 0 1) (cons 2 3))  ; => ((0 . 1) 2 . 3)
