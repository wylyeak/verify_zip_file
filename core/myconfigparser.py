from configobj import ConfigObj


class MyConfigParser(ConfigObj):
    def __init__(self, infile=None, options=None, configspec=None, encoding=None,
                 interpolation=True, raise_errors=False, list_values=True,
                 create_empty=False, file_error=False, stringify=True,
                 indent_type=None, default_encoding=None, unrepr=False,
                 write_empty_values=False, _inspec=False):
        super(MyConfigParser, self).__init__(infile, options, configspec, encoding,
                                             interpolation, raise_errors, list_values,
                                             create_empty, file_error, stringify,
                                             indent_type, default_encoding, unrepr,
                                             write_empty_values, _inspec)
        self.cfg_path = infile


if __name__ == "__main__":
    cf = MyConfigParser("../config/config.ini")
    print cf.get("123")
    print cf.get("exclude_txt")
    for section in cf.sections:
        for entry in cf[section]:
            print cf[section][entry]
