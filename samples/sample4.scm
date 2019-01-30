; quote 式
; 引数１つを評価せずにそのまま返す

(quote 1)                  ; => 1
(quote (+ 1 2 3))          ; => (+ 1 2 3) 
(quote a)                  ; => a
(quote (+ a b c))          ; => (+ a b c)
(quote (print (+ a b c)))  ; => (print (+ a b c))

; ' を用いた時も同様
'1                  ; => 1
'(+ 1 2 3)          ; => (+ 1 2 3) 
'a                  ; => a
'(+ a b c)          ; => (+ a b c)
'(print (+ a b c))  ; => (print (+ a b c))
