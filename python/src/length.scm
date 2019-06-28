(define length (lambda (lst) (cond ((is_null lst) 0) (else (add 1 (length (cdr lst)))))))
