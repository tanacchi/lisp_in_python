from unittest import TestCase
from src import lisp01


class TestLisp01(TestCase):
    def setUp(self):
        self.evaluator = lisp01.Evaluator()

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

    def test_multi_evaluator01(self):
        eval_args = ['*', 2, 3]
        self.assertEqual(lisp01.evaluate(eval_args), 2*3)

    def test_multi_evaluator02(self):
        eval_args = ['*', 5, 3, 4]
        self.assertEqual(lisp01.evaluate(eval_args), 5*3*4)

    def test_div_evaluator01(self):
        eval_args = ['/', 10, 2]
        self.assertEqual(lisp01.evaluate(eval_args), 10/2)

    def test_div_evaluator02(self):
        eval_args = ['/', 12, 3, 2]
        self.assertEqual(lisp01.evaluate(eval_args), 12/3/2)
