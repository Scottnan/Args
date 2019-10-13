import unittest
from main.Parser import ArgsParser, Schema


class MyTestCase(unittest.TestCase):
    def test_parse_text_to_dict(self):
        # TODO: parse input
        args_as_text = "-l -p 8080 -d /usr/logs"
        args_as_dict = ArgsParser().parse(args_as_text)

    def test_dict_type(self):
        # TODO: check args type
        schema_as_text = "l:boolean p:integer d:string"
        schema = Schema(schema_as_text)

    def test_get_args_value(self):
        # TODO: check value
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
