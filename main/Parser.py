import re
import copy


class ArgsParser(object):
    def __init__(self, command):
        self._schema = None
        self._command = Command(command)

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema_as_text):
        if not isinstance(schema_as_text, str):
            raise TypeError("expected a string")
        self._schema = Schema(schema_as_text)

    def _convert_str_to_arg_type(self, arg):
        try:
            if self._schema.get_type(arg) == 'bool':
                if self._command.get_value(arg) is None:
                    return True
                else:
                    return bool(self._command.get_value(arg))
            elif self._schema.get_type(arg) == 'int':
                return int(self._command.get_value(arg))
            else:
                return self._command.get_value(arg)
        except ValueError:
            print("please check type of %s" % arg)

    def get_args(self, arg):
        res = self._convert_str_to_arg_type(arg)
        return res


class Command(object):
    def __init__(self, command_line):
        self.arg_dict = {}
        command_iter = iter(re.split(r"\s+", command_line))
        try:
            while True:
                arg = next(command_iter)[1]
                previous, command = copy.deepcopy(command_iter), next(command_iter)
                if self._is_value(command):
                    self.arg_dict[arg] = command
                else:
                    command_iter = previous
        except StopIteration:
            pass

    def get_value(self, arg):
        return self.arg_dict.get(arg, None)

    @staticmethod
    def _is_value(command):
        if command[0] != '-':
            return True
        elif "0" <= command[1] <= "9":
            return True
        else:
            return False


class Schema(object):
    def __init__(self, schema_as_text):
        schema = schema_as_text.split(" ")
        self.schema_dict = {}
        for i in schema:
            key, val = i.split(":")
            self.schema_dict[key] = val

    def get_type(self, arg):
        if arg not in self.schema_dict.keys():
            raise ValueError("unexcept argument %d" % arg)
        return self.schema_dict[arg]