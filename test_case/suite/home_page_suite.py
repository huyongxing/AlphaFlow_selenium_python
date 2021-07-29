#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm


from test_case.suite import *


def suite():
    suite = unittest.TestSuite()
    suite.addTest(home_page_case.home_page_case('test_loginsSuccess'))
    return suite
