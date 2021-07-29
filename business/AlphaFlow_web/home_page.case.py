#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

from business.AlphaFlow_web import *

if __name__ == '__main__':
    suite_tests = home_page_suite.suite()
    report_name = "测试报告"
    description = "首页测试"
    result = Report.report(suite_tests, report_name, description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")
