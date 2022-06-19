# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/12 13:52
@Auth ： ghm
@File ：connect_iphone.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from poco.drivers.android.uiautomation import AndroidUiautomationPoco  # 不同的手机系统使用不同的库不一样
from airtest.core.api import *  # connect_device()  start_app()  clear_app()
from common.basepage import *
import time


class Open_iphone(object):

    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    def start_app(self):
        # 链接手机
        # connect_device('Android:///182QGFZL2244A')
        # 什么都不填写，会默认取当前连接中的第一台手机
        # connect_device('Android:///')
        # # 连接本机默认端口连的一台设备号为79d03fa的手机  没试验过
        # connect_device('Android:///127.0.0.1:5037/79d03fa')
        # # 连接一个Windows窗口，窗口句柄为123456      没试验过
        # connect_device('Windows:///123456')

        start_app('com.ss.android.article.news')
        self.poco(name="com.ss.android.article.news:id/dbq").swipe(direction='up',duration=2)

        # stop_app('com.ss.android.article.news')


if __name__ == '__main__':
    Open_iphone().start_app()