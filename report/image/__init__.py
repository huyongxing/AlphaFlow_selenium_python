#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

import os
import time
from function.driver import *


# 生成年月日时分秒时间
def catch_image(driver):
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # 打印文件目录
    root_path = os.path.abspath(os.path.dirname(__file__)).split('AlphaFlow_selenium_python')[0]
    # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        File_Path = root_path + '\\AlphaFlow_selenium_python\\report\\image\\' + directory_time + '\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
    except BaseException as msg:
        print("新建目录失败：%s" % msg)

    try:
        driver.save_screenshot(
            root_path + '\\AlphaFlow_selenium_python\\report\\image\\' + directory_time + '\\' + picture_time + '.png')
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)
