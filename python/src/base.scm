(define nil
  (quote ()))

(define null?
  (lambda (lst)
    (eq? lst nil)))

(define zero? 
  (lambda (num) 
    (eq? num 0)))

(define #t
  (null? nil))

(define #f
  (null? (quote (ahi))))

(define not
  (lambda (x)
    (cond
      (x    #f)
      (else #t))))

(define and
  (lambda (x y)
    (cond
      (x y)
      (else #f))))

(define or
  (lambda (x y)
    (cond
      (x #t)
      (else y))))

(define list
  (lambda (x)
    (cons x nil)))

(define reverse
  (lambda (lst)
    (define reverse-aux
      (lambda (lst result)
        (cond
          ((null? lst) result)
          (else (reverse-aux (cdr lst) (cons (car lst) result))))))
    (reverse-aux lst (quote ()))))
