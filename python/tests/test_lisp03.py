from unittest import TestCase
from src import lisp03


class TestLisp01(TestCase):
    def setUp(self):
        self.reader = lisp03.Reader()

    def test_simple_simple_reader(self):
        result = self.reader.read("( 1 2 3 )");
        self.assertEqual(result, ["1", "2", "3"]);
