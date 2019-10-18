import unittest
from main.Parser import Command


class MyTestCase(unittest.TestCase):
    def test_has_value(self):
        command = Command("-l True -p 8080 -d /usr/logs")
        self.assertEqual("True", command.get_value("l"))
        self.assertEqual("8080", command.get_value("p"))
        self.assertEqual("/usr/logs", command.get_value("d"))

    def test_no_value(self):
        command = Command("-l -p 8080 -d /usr/logs")
        self.assertEqual(None, command.get_value("l"))
        self.assertEqual("8080", command.get_value("p"))
        self.assertEqual("/usr/logs", command.get_value("d"))

    def test_has_negative_value(self):
        command = Command("-l -p -9 -d /usr/logs")
        self.assertEqual(None, command.get_value("l"))
        self.assertEqual("-9", command.get_value("p"))
        self.assertEqual("/usr/logs", command.get_value("d"))


if __name__ == '__main__':
    unittest.main()
