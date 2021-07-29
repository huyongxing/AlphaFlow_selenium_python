#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

from function.customize import *
from function.config import *


class Data():
    def __init__(self):
        self.url = get("url", "web_url")
        self.sms_code = '123456'

    def get_account(self, account):
        self.result = get("account", account)
        return self.result

    def get_pwd(self, pwd):
        self.result = get("pwd", pwd)
        return self.result

    def get_userinfo(self):
        self.userinfo = User()
        return self.userinfo


if __name__ == '__main__':
    try:
        a = Data()
        print(a.get_userinfo().name)
        print(a.get_account("rt_account"))
        print(a.get_pwd("rt_pwd"))
    except Exception as e:
        print("")
