#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

import os,math

if __name__ == '__main__':
    try:
        cmd = 'taskkill /F /IM chromedriver.exe'
        os.system(cmd)


    except Exception as e:
        print(e)
