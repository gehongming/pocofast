import logging
from common.poco_path import LOG_DIR
from common.poco_config import *
import time

config = ReadConfig()


class HandleLogger:
    """处理日志相关的模块"""

    @staticmethod
    def create_logger():
        """
        创建日志收集器
        :return: 日志收集器
        """
        # 第一步：创建一个日志收集器
        log = logging.getLogger("poco")

        # 第二步：设置收集器收集的等级
        log.setLevel(config.get("log", "level"))

        log_name = config.get("log", "filename")

        # 第三步：设置输出渠道以及输出渠道的等级
        curTime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        fh = logging.FileHandler(LOG_DIR + f"/{log_name}_{curTime}.log", encoding="utf8")
        fh.setLevel(config.get("log", "fh_level"))
        log.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(config.get("log", "sh_level"))
        log.addHandler(sh)
        # 创建一个输出格式对象
        formats = '%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        form = logging.Formatter(formats)
        # 将输出格式添加到输出渠道
        fh.setFormatter(form)
        sh.setFormatter(form)

        return log


if __name__ == '__main__':

    logo = HandleLogger.create_logger()
    logo.info('haha')
