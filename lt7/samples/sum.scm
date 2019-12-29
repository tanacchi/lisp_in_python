(define sum
  (lambda (lst)
    (if (null? lst)
      0
      (+ (car lst) (sum (cdr lst))))))
