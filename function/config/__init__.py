#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

import os
from function import *
from report import *


def get(title, string):
    try:
        root_path = os.path.abspath(os.path.dirname(__file__)).split('AlphaFlow_selenium_python')[0]
        path = root_path + "\\AlphaFlow_selenium_python\\function\\config"
        config = configparser.ConfigParser()
        config.read(path + "\\Config.ini")
        result = config.get(title, string)
        return result
    except Exception as e:
        logging.error("获取配置报错：" + e)


if __name__ == '__main__':
    print(get("url", "web_url"))
    print(get("account", "rt_account"))
