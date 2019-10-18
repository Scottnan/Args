import unittest
from main.Parser import Schema


class MyTestCase(unittest.TestCase):
    def test_set_schema(self):
        schema_as_text = "l:bool p:int d:str"
        schema = Schema(schema_as_text)
        self.assertEqual("bool", schema.get_type("l"))
        self.assertEqual("int", schema.get_type("p"))
        self.assertEqual("str", schema.get_type("d"))


if __name__ == '__main__':
    unittest.main()
