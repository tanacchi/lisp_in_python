from unittest import TestCase
from lisp import lisp01


class TestLisp01(TestCase):
    def test_plus_evaluator01(self):
        eval_args = ['+', 1]
        self.assertEqual(lisp01.evaluate(eval_args), 1)

    def test_plus_evaluator02(self):
        eval_args = ['+', 1, 2]
        self.assertEqual(lisp01.evaluate(eval_args), 1+2)

    def test_plus_evaluator03(self):
        eval_args = ['+', 1, 2, 3]
        self.assertEqual(lisp01.evaluate(eval_args), 1+2+3)

    def test_minus_evaluator01(self):
        eval_args = ['-', 1, 2]
        self.assertEqual(lisp01.evaluate(eval_args), 1-2)

    def test_minus_evaluator02(self):
        eval_args = ['-', 5, 3, 3]
        self.assertEqual(lisp01.evaluate(eval_args), 5-3-3)

