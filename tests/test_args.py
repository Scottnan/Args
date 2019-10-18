import unittest
from main.Parser import ArgsParser


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.args_parser = ArgsParser("-l -p 8080 -d /usr/logs")
        cls.args_parser.schema = "l:bool p:int d:str"

    def test_get_args_value(self):
        self.assertEqual(True, self.args_parser.get_args("l"))
        self.assertEqual(8080, self.args_parser.get_args("p"))
        self.assertEqual("/usr/logs", self.args_parser.get_args("d"))


if __name__ == '__main__':
    unittest.main()
