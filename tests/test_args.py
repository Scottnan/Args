import unittest
from main.Parser import ArgsParser, Schema


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.args_parser = ArgsParser()
        cls.args_parser.schema = "l:bool p:int d:str"

    def test_set_schema(self):
        # TODO: check args type
        schema_as_text = "l:bool p:int d:str"
        schema = Schema(schema_as_text)
        self.assertEqual("bool", schema.get_type("l"))
        self.assertEqual("int", schema.get_type("p"))
        self.assertEqual("str", schema.get_type("d"))

    def test_args_type(self):
        # TODO: check args type
        self.assertEqual(("bool", "l", True), self.args_parser._check_arg_type("l"))
        self.assertEqual(("int", "p", 8080), self.args_parser._check_arg_type("p 8080"))
        self.assertEqual(("str", "d", "/usr/logs"), self.args_parser._check_arg_type("d /usr/logs"))

    def test_get_args_value(self):
        # TODO: check value
        args_as_text = "-l -p 8080 -d /usr/logs"
        self.args_parser.parse(args_as_text)
        self.assertEqual(True, self.args_parser.get_args("l"))
        self.assertEqual(8080, self.args_parser.get_args("p"))
        self.assertEqual("/usr/logs", self.args_parser.get_args("d"))


if __name__ == '__main__':
    unittest.main()
