class ArgsParser(object):
    def __init__(self):
        self.args_dict = {}
        self._schema = None

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema_as_text):
        if not isinstance(schema_as_text, str):
            raise TypeError("expected a string")
        self._schema = Schema(schema_as_text)

    def _check_arg_type(self, arg):
        if self.schema is None:
            raise ValueError("please set schema")
        if len(arg) == 1:
            arg_name = arg
            arg_type = self.schema.get_type(arg)
            val = ''
        else:
            arg_name, val = arg.split(" ")
            arg_type = self.schema.get_type(arg_name)
        if arg_type == "bool" and val == '':
            return arg_type, arg_name, True
        try:
            arg_val = eval(arg_type)(val)
        except ValueError:
            raise TypeError("argument {} should be {}".format(arg_name, arg_type))
        return arg_type, arg_name, arg_val

    def get_args(self, arg):
        return self.args_dict[arg]

    def parse(self, args_as_text):
        args_as_list = args_as_text.split("-")
        args_as_list.remove("")
        for arg in args_as_list:
            print(arg)
            arg_type, arg_name, arg_val = self._check_arg_type(arg.strip())
            self.args_dict[arg_name] = arg_val


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