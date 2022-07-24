# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/19 17:15
@Auth ： ghm
@File ：login_toutiao.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True)


class HomeLocators:

    def __init__(self, poco):
        self.poco = poco

    def page(self):

        tuijian = self.poco(name='推荐')
        tuijianpage = self.poco(name="androidx.recyclerview.widget.RecyclerView")
        return tuijian, tuijianpage
