from unittest import TestCase

import sys
sys.path.append('../')

from src.reader import Reader
from src.evaluator import evaluate
from src.env import Env

class TestBaseLibrary(TestCase):
    def setUp(self):
        self.env = Env()
        self.env.update({
            'add1': lambda args : args[0] + 1,
            'sub1': lambda args : args[0] - 1
        })

        load_command_str = "(load \"../src/base.scm\")"
        evaluate(Reader.parse(load_command_str), self.env)
    
    def test_null_check(self):
        with open("../../scheme/add1.scm") as f:
            print(f.path())
            command_list = Reader.parse(f.read())
            for command in command_list:
                result = evaluate(command, self.env)
                self.assertEqual(result, True)
