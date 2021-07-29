#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm


from function import *

root_path = os.path.abspath(os.path.dirname(__file__)).split('AlphaFlow_selenium_python')[0]


class Driver():
    def __init__(self):
        self.driver_path = root_path + "\\AlphaFlow_selenium_python\\function\\driver\\chromedriver.exe"
        self.chrome_browser = webdriver.Chrome(self.driver_path)
        self.chrome_browser.maximize_window()
        self.chrome_browser.implicitly_wait(30)

    def tearDown(self):
        self.chrome_browser.quit()


def upload_image(file_dir, file_name):
    time.sleep(0.5)
    up_load_path = root_path + "\\AlphaFlow_selenium_python\\function\\driver\\upimage.exe"
    file_path = file_dir + file_name + '.png'
    os.system('%s  %s' % (up_load_path, file_path))  # 调用AutoIt进行上传操作


if __name__ == '__main__':
    browser = Driver()
    url = "https://huaweiyun.flowyun.com:1443/login"
    browser.chrome_browser.get(url)
    browser.tearDown()
