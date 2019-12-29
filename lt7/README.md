# lt7

## What is this?
Python で実装された Lisp ライクなインタプリタ型言語．  
理解のしすさのために，インクリメンタル開発をベースとした構成になっている．  
テスト駆動開発と相性が良さそうだけど導入はしていない．  
level15 の変数スコープは発表では間に合わないかもしれない．  

## primitives

format | type
--- | ---
`[+-]?[0-9]+` | int
`[+-]?[0-9]+\.[0-9]*` | float
`#true`\|`#false` | bool
other | str

## keywords

name |first appearance | example
--- | --- | ---
`define` | level 07 | `(define x 3)` (x = 3)
`lambda` | level 10 | `(lambda (varg) expr)` -> `<lambda-function>`
`eq?` | level 11 | `(eq? 0 0)` -> `True`
`if` | level 12 | `(if condition true_value false_value)`
`quote` | level 13 | `(quote (0 1 2))` -> `(0 1 2)`
`car` | level 14-1 | `(car x)` -> `x[0]`
`cdr` | level 14-2 | `(cdr x)` -> `x[1:]`
`cons` | level 14-3 | `(cons new x)` -> `(new x[0] x[1] ..)`

## built-in variables and functions
name | first appearance | example
--- | --- | ---
`+` | level 06 | `(+ 3 4)` -> `7`
`-` | level 06 | `(- 8 5)` -> `3`
`#true` | level 11 | `True`
`#false` | level 11 | `False`

## level

level | description
--- | ---
level 01 | あいさつ
level 02 | プロンプトとループ
level 03 | 字句解析器
level 04 | 構文解析器
level 05 | 評価器(evaluate 関数)
level 06 | 加減算
level 07 | 変数定義
level 08 | 変数の参照
level 09 | 関数呼び出し
level 10 | 関数定義 (add1, sum-of-three 実装)
level 11 | 比較 (zero? 実装)
level 12 | 分岐 (not 実装)
level 13 | quote と list (null? 実装)
level 14 | リスト操作 (sum, length  実装)
level 15 | 変数スコープ (reverse, range 実装)

## sample code
### arithmetic operation
```Scheme
(+ 3 4)  ;-> 7

(define x 42)
(define y 31)
(- x y)  ;-> 11
```

### add1
```Scheme
(define add1
  (lambda (x)
    (+ x 1)))


(add1 9)  ;-> 10

(define x 41)
(add1 x)  ;-> 42
```

## sum-of-three
```Scheme
(define sum-of-three
  (lambda (x y z)
    (+ x (+ y z))))


(sum-of-three 3 6 1)  ;-> 11
```

### zero?
```Scheme
(define zero?
  (lambda (x)
    (eq? x 0)))


(zero? 3)  ;-> False

(define x 0)
(zero? x)  ;-> True
```

### not
```Scheme
(define not
  (lambda (x)
    (if x #false
          #true)))


(not (eq? 0 0))  ;-> False

(define x (eq? 0 1))
(not x)  ;-> True
```

### null?
```Scheme
(define null?
  (lambda (x)
    (eq? x (quote ()))))


(null? (quote (1 2 3)))  ;-> False

(define empty-list (quote ()))
(null? empty-list)  ;-> True
```

### sum
```Scheme
; requires 'null?'

(define sum
  (lambda (list)
    (if (null? list)
      0
      (+ (car list) (sum (cdr list))))))


(sum (quote (1 2 3)))  ;-> 6

(define x (quote (1 2 3 4 5 6 7 8 9 10)))
(sum x)  ;-> 55
```

### length
```Scheme
; requires 'null?', 'add1'

(define length
  (lambda (x)
    (if (null? x) 
      0
      (add1 (length (cdr x))))))


(length (quote ()))  ;-> 0

(define lst (quote (0 1 2 3 4 5 6 7 8 9)))
(length lst)  ;-> 10
```

### reverse
```Scheme
; requires 'null?'

(define reverse
  (lambda (x)
    (define reverse-aux
      (lambda (x result)
        (if (null? x)
          result
          (reverse-aux (cdr x) (cons (car x) result)))))
    (reverse-aux x (quote ()))))


(reverse (quote ()))  ;-> ()

(define lst (quote (0 1 2 3 4 5 6 7 8 9)))
(reverse lst)  ;-> (9 8 7 6 5 4 3 2 1 0)
```

### range
```Scheme
; requires 'zero?', 'sub1', 'reverse'

(define range
  (lambda (n)
    (define range-aux
      (lambda (n)
        (if (zero? n)
          (quote ())
          (cons (sub1 n) (range-aux (sub1 n))))))
    (reverse (range-aux n))))
    

(range 10)  ;-> (0 1 2 3 4 5 6 7 8 9)
```
