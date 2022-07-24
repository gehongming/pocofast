# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/19 17:17
@Auth ： ghm
@File ：home_tuijian.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from common.basepage import *
from pagelocators.home_toutiao import *


class HomePage(BasePage):

    def ClickTuijian(self):
        self.click_element(loc=HomeLocators(poco=self.poco).page()[0])

    def LongClickTuijian(self):
        self.long_click_element(loc=HomeLocators(poco=self.poco).page()[0], duration=3)

    def Swipehome(self):
        self.swipe(loc=HomeLocators(poco=self.poco).page()[1], direction='up', duration=3)


if __name__ == '__main__':
    from airtest.core.api import *
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    start_app('com.ss.android.article.news')
    # HomePage().ClickTuijian()
    # HomePage().LongClickTuijian()
    HomePage(poco=poco).Swipehome()