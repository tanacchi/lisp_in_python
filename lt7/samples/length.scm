(define nil (quote ()))

(define null?
  (lambda (x)
    (eq? x nil)))

(define add1
  (lambda (x)
    (+ x 1)))

(define length
  (lambda (x)
    (if (null? x)
      0
      (add1 (length (cdr x))))))
