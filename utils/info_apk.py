# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/12 14:20
@Auth ： ghm
@File ：info_apk.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from math import floor
import os
import subprocess


class ApkInfo:
    # 待测试应用路径
    apkPath = "D:\Downloads\\toutiao.apk"

    def __init__(self):
        # self.aapt = "D:\\ProgramFiles\\android-sdk-windows\\build-tools\\28.0.3\\aapt dump badging "
        self.aapt = "F:\\aapt\\aapt.exe dump badging "

    # 获取app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkPath)/(1024*1000))
        return str(size) + "M"

    # 获取app的版本信息
    def get_apk_version(self):
        cmd = self.aapt + self.apkPath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[3].decode()[12:]
            result = result.split("'")[1]
        return result

    # 获取app的名字
    def get_apk_name(self):
        cmd = self.aapt + self.apkPath + " | findstr application-label-zh_CN: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, encoding='utf8')
        if output != "":
            result = output.split("'")[1]
        return result

    # 获取app的包名
    def get_apk_package(self):
        cmd = self.aapt + self.apkPath + " | findstr package:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, encoding='utf8')
        if output != "":
            result = output.split()[1][6:-1]
        return result

    # 得到启动类
    def get_apk_activity(self):
        cmd = self.aapt + self.apkPath + " | findstr launchable-activity:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result


if __name__ == '__main__':
    apkInfo = ApkInfo()
    print("应用名称:", apkInfo.get_apk_name())
    print("app文件大小:", apkInfo.get_apk_size())
    print("app版本信息:", apkInfo.get_apk_version())
    print("app包名:", apkInfo.get_apk_package())
    print("app的启动类:", apkInfo.get_apk_activity())