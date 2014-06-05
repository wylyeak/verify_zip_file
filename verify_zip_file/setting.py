from myconfigparser import MyConfigParser


class Settings(object):
    def __init__(self, cfg_path):
        super(Settings, self).__init__()
        self.cf = MyConfigParser(cfg_path)

    def get_file_config_path(self, file_name):
        for name in self.cf["file_config_mapper"]:
            value = self.cf["file_config_mapper"][name]
            if file_name.find(name) >= 0:
                return value
        return None

    def set_config_mapper(self, name, value):
        self.cf["file_config_mapper"][name] = value
        self.cf.write()

    def del_config_mapper(self, name):
        del self.cf["file_config_mapper"][name]
        self.cf.write()


if __name__ == "__main__":
    settings = Settings("setting.ini")
    assert None == settings.get_file_config_path("123123123-www.google.com.hk-2123123123.zip")
    settings.set_config_mapper("www.google.com.hk", "config1.ini")
    assert "config1.ini" == settings.get_file_config_path("123123123-www.google.com.hk-2123123123.zip")
    settings.del_config_mapper("www.google.com.hk")
    assert None == settings.get_file_config_path("123123123-www.google.com.hk-2123123123.zip")
    print "test success"