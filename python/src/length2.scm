(define length2 (lambda (lst) (define length2_aux (lambda (lst result) (cond ((is_null lst) result) (else (length2_aux (cdr lst) (add 1 result)))))) (length2_aux lst 0)))
