#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

import os
if __name__ == '__main__':
    print(os.system('%s' % ("pyinstaller -F  home_page.case.py")) ) # 调用s_AutoIt进行上传操作