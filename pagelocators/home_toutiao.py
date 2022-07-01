# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/19 17:15
@Auth ： ghm
@File ：login_toutiao.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True)


class HomeLocators:

    tuijian = poco(name='推荐')
    tuijianpage = poco(name="androidx.recyclerview.widget.RecyclerView")


