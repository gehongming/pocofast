# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/5 22:05
@Auth ： ghm
@File ：basepage.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import time
import os
import datetime
from airtest.core.api import snapshot
from common import poco_log  # 直接执行了logger里的代码。设置日志输出。
from common import poco_path

logging = poco_log.HandleLogger.create_logger()


class BasePage:

    def __init__(self, poco):  # 传入连接的手机  from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        self.poco = poco

    # 等待一定时间内判断元素存在
    def ele_exists(self, loc, img_desc='默认判断', timeout=0.5):
        """

        :param loc:
        :param img_desc: 元素的名称截图用
        :param timeout:
        :param frequency:
        :return:
        """
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            loc.refresh()  # 节点刷新 放置节点过期
            loc.wait(timeout=timeout).exists()
        except:
            # 日志
            logging.exception("元素 {} 不存在！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("判断 {}  元素  {} 存在。耗时：{}".format(img_desc, loc, end - start))
        return loc

    # 点击元素
    def click_element(self, loc, img_desc='默认点击', timeout=0.5, focus=None, sleep_interval=None):
        """

        :param loc:
        :param img_desc:
        :param timeout:
        :param focus: 值为：(x,y)或“anchor”或“center”。为None默认点击在 anchorPoint
        :param sleep_interval: 点击操作后等待的秒数。默认值为无，这里默认睡眠间隔。这个值可以通过POCO初始化进行配置。
        :return:
        """
        ele = self.ele_exists(loc, img_desc, timeout)
        # 操作
        try:
            ele.click(focus=focus, sleep_interval=sleep_interval)  # 点击操作
            logging.info("点击  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("点击  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 长按
    def long_click_element(self, loc, img_desc='默认长按', timeout=0.5, duration=2.0):
        """
        :param duration: 长按时间
        :return:
        """
        ele = self.ele_exists(loc, img_desc, timeout)
        # 操作
        try:
            ele.long_click(duration=duration)  # 操作
            logging.info("长按  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("长按  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 输入文字
    def input_text(self, loc, value, img_desc='默认输入', timeout=0.5):
        ele = self.ele_exists(loc, img_desc, timeout)
        # 操作
        try:
            ele.set_test(value)  # 点击操作
            logging.info("在 {} 元素 {} 上输入文本值：{} 成功！".format(img_desc, loc, value))
        except:
            # 日志
            logging.exception("在 {} 元素 {} 上输入文本值：{} 失败！".format(img_desc, loc, value))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 滑动
    def swipe(self, loc, img_desc='默认滑动', focus=None, direction='up', duration=0.5, timeout=0.5):
        """

        :param loc: 已他为重心滑动，调试的时候用的页面
        :param img_desc:
        :param focus:
        :param direction:up=[0, -0.1]，down=[0, 0.1]，left=[-0.1, 0]，right=[0, 0.1]
        :param duration: 滑动持续时间
        :param timeout:
        :return:
        """

        ele = self.ele_exists(loc, img_desc, timeout)
        # 操作
        try:
            ele.swipe(direction=direction, focus=focus, duration=duration)  # 点击操作
            logging.info("在 {} 元素 {} 上滑动成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("在 {} 元素 {} 上滑动失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_desc, timeout=0.5):
        """

        :param loc:
        :param attr_name: 节点的属性名的key，例如 tepy，text，enabled
        :param img_desc:
        :param timeout:
        :param frequency:
        :return:
        """
        ele = self.ele_exists(loc, img_desc, timeout)
        # 获取属性
        try:
            attr_value = ele.attr(attr_name)
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的属性 {} 失败！".format(img_desc, loc, attr_name))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的属性 {} 值为:{}".format(img_desc, loc, attr_name, attr_value))
            return attr_value

    # 获取元素的文本值。
    def get_text(self, loc, img_desc, timeout=0.5):
        ele = self.ele_exists(loc, img_desc, timeout)
        # 获取属性
        try:
            text = ele.get_text()
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的文本失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的文本值为:{}".format(img_desc, loc, text))
            return text

    # 截图
    def save_img(self, img_description):
        """
        :param img_description: 图片的描述 。格式为 页面名称_功能名
        :return:
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 时间戳 time模块  不要有:
        filepath = "{}_{}.png".format(img_description, now)
        img_path = os.path.join(poco_path.SCREENSHOT_DIR, filepath)
        try:
            snapshot(filename=f'{img_path}')
        except:
            logging.exception("网页截图失败！")
        else:
            logging.info("截图成功，截图存放在：{}".format(img_path))

    # 列表滑动
    # toast
    # h5切换
    # 应用切换
    # robot框架当中，有更丰富的封装。


