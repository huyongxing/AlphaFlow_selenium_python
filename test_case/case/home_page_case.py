#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm


from test_case.case import *


class home_page_case(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.browser = self.driver.chrome_browser
        self.log = Logs()
        self.data = Data()
        self.image = Image()  # 初始化截屏功能

    def login(self):
        try:
            data = Data()
            url = data.url
            self.browser.get(url)
        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_loginbypw(self):
        try:
            data = Data()
            account = data.get_account("rt_account")
            pwd = data.get_pwd("rt_pwd")
            find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[0].send_keys(account)
            find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[1].send_keys(pwd)
            find_element(self.browser, By.XPATH, "//span[text()='登录']").click()
        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_quick_start(self):
        self.login()
        self.test_loginbypw()
        time.sleep(1)

    def tearDown(self):
        self.log.log_info("首页测试结束")
        time.sleep(3)
        self.driver.tearDown()


if __name__ == '__main__':
    unittest.main()
