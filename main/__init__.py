#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

import os,sys

if __name__ == '__main__':
    # print(os.system('%s' % ("pip freeze > requirements.txt")))

    print(os.system('%s' % ("pip install -r requirements.txt")))