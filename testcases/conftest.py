# __author__="G"
#date: 2019/6/29
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/6/20

import pytest

from airtest.core.api import *


# session级别的
@pytest.fixture(scope="session", autouse=True)  # 默认调用
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    # 清除测试报告、截图目录
    # remove_files_in_dir(contants.reports_screen)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")


@pytest.fixture(scope="class")
def open_url_clink_ol():
    # 前置
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    auto_setup(__file__, devices=["android://127.0.0.1:5037/127.0.0.1:7555"])
    poco = AndroidUiautomationPoco(use_airtest_input=True)
    yield poco



# @pytest.fixture(scope="class")
# def open_url_m():
#     mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('mobileEmulation', mobileEmulation)
#     driver = webdriver.Chrome(
#         executable_path='chromedriver.exe',
#         options=options)
#     driver.get(cd.base_url_m)
#     yield driver
#     driver.quit()
