from unittest import TestCase
from src import reader
from src import main

class TestBaseLibrary(TestCase):
    def setUp(self):
        self.env = main.Env()
        self.env.update({
            'add1': lambda args : args[0] + 1,
            'sub1': lambda args : args[0] - 1
        })

        load_command_str = "(load \"base.scm\")"
        main.evaluate(main.Reader.parse(load_command_str), env)
    
    def test_null_check(self):
        with open("scheme/null.scm") as f:
            command_list = main.Reader.parse(f.read())
            for command in command_list:
                result = main.evaluate(command, env)
                self.assertEqual(result, True)
