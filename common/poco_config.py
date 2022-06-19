import configparser
import os
from common import poco_path


class ReadConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(poco_path.GLOBAL_FILE)
        switch = self.config.get('switch', 'on')  # 读取value
        file = os.path.join(poco_path.BASE_DIR, "config", f'config_{switch.lower()}.ini')
        self.config.read(file, encoding='utf-8')

    def get(self, section, option):
            return self.config.get(section,option)


class WriteConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(poco_path.GLOBAL_FILE,encoding='utf-8')

    def write(self, value, section='switch', option='on'):
            self.config.read(poco_path.GLOBAL_FILE)
            self.config.set(section, option, value)
            file_global = os.path.join(poco_path.GLOBAL_FILE)
            with open(file_global, 'w') as wf:
                self.config.write(wf)


# config = ReadConfig()
if __name__ == '__main__':
    # wr = WriteConfig()
    # on = wr.write(value='test8')
    config = ReadConfig()
    host = config.get("log", "level")
    print(host)

    # number = int(config.get("data", "chatLimitNumber"))
    # print(number)