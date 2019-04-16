from unittest import TestCase
from src import lisp02


class TestLisp01(TestCase):
    def setUp(self):
        pass

    def test_linked_list_string(self):
        args = [1, 2]
        list = lisp02.LinkedList(args)
        self.assertEqual(str(list), "( 1 . 2 )")
