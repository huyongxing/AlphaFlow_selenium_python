#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

from test_case.case import *


class Login_Case(unittest.TestCase):
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

    # def test_loginbysms(self):
    #     try:
    #         data = Data()
    #         account = data.get_account("account")
    #         sms_code = data.sms_code
    #         find_elements(self.browser, By.CLASS_NAME, "ant-tabs-tab-btn").click()
    #         find_elements(self.browser, By.CLASS_NAME, "ant-input u-input-big")[0].send_keys(account)
    #         find_elements(self.browser, By.XPATH, "//*[@id='rc-tabs-0-panel-2']/div/div[2]/div/div[2]/button/span").click()
    #         find_elements(self.browser, By.CLASS_NAME, "ant-input u-input-mid f-fl").send_keys(sms_code)
    #         find_elements(self.browser, By.TAG_NAME, "button")[0].click()
    #     except Exception as e:
    #         print(e)
    #         catch_image(self.browser)

    def test_loginAccountPwMenu(self):
        '''账号密码登录菜单'''
        self.login()
        AccountPdMenu = find_element(self.browser, By.ID, "rc-tabs-0-tab-1").text
        self.assertEqual(AccountPdMenu, "账号密码登录")

    def test_loginAccountInputBox(self):
        '''账号输入框提示'''
        self.login()
        AccountInputBox = find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[
            0].get_attribute('placeholder')
        self.assertEqual(AccountInputBox, "手机号/电子邮箱")

    def test_loginPwInputBox(self):
        '''密码输入框提示'''
        self.login()
        PwInputBox = find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[1].get_attribute(
            'placeholder')
        self.assertEqual(PwInputBox, "密码")

    def test_loginBotton(self):
        '''登录按钮'''
        self.login()
        loginBotton = find_element(self.browser, By.XPATH, "//span[text()='登录']").text
        self.assertEqual(loginBotton, "登录")

    def test_loginOtherWays(self):
        '''其他登录方式'''
        self.login()
        loginOtherWays = find_element(self.browser, By.XPATH, "//span[text()='其他登录方式']").text
        self.assertEqual(loginOtherWays, "其他登录方式")

    def test_loginForgetPw(self):
        '''忘记密码按钮'''
        self.login()
        ForgetPw = find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").text
        self.assertEqual(ForgetPw, "忘记密码")

    def test_loginAccountLack(self):
        '''账号缺失提示'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='登录']").click()
        AccountLack = find_element(self.browser, By.XPATH, "//span[text()='请输入账号']").text
        self.assertEqual(AccountLack, "请输入账号")

    def test_loginAccountError(self):
        '''账号错误提示'''
        self.login()
        find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[0].send_keys(1350376111)
        find_element(self.browser, By.XPATH, "//span[text()='登录']").click()
        AccountError = find_element(self.browser, By.XPATH, "//span[text()='账号格式错误']").text
        self.assertEqual(AccountError, "账号格式错误")

    def test_loginPwLack(self):
        '''密码缺失提示'''
        self.login()
        find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[0].send_keys(13712666007)
        find_element(self.browser, By.XPATH, "//span[text()='登录']").click()
        PwLack = find_element(self.browser, By.XPATH, "//span[text()='请输入密码']").text
        self.assertEqual(PwLack, "请输入密码")

    def test_loginPwError(self):
        '''密码错误提示'''
        self.login()
        find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[0].send_keys(13712666007)
        find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[1].send_keys(111111)
        find_element(self.browser, By.XPATH, "//span[text()='登录']").click()
        PwError = find_element(self.browser, By.XPATH, "//span[text()='用户密码错误']").text
        self.assertEqual(PwError, "用户密码错误")

    def test_loginVerificaCode(self):
        '''验证码登录菜单'''
        self.login()
        VerificaCode = find_element(self.browser, By.ID, "rc-tabs-0-tab-2").text
        self.assertEqual(VerificaCode, "验证码登录")

    def test_loginVCAccountInputBox(self):
        '''验证码登录-账号输入框提示'''
        self.login()
        find_element(self.browser, By.ID, "rc-tabs-0-tab-2").click()
        VCAccountInputBox = find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[
            2].get_attribute('placeholder')
        self.assertEqual(VCAccountInputBox, "手机号/电子邮箱")

    def test_loginVCodeInputBox(self):
        '''验证码登录-验证码输入框提示'''
        self.login()
        find_element(self.browser, By.ID, "rc-tabs-0-tab-2").click()
        VCodeInputBox = find_element(self.browser, By.XPATH,
                                      "//input[@class='ant-input u-input-mid f-fl']").get_attribute('placeholder')
        self.assertEqual(VCodeInputBox, "请输入验证码")

    def test_loginGetCodeButton(self):
        '''验证码登录-获取验证码按钮'''
        self.login()
        find_element(self.browser, By.ID, "rc-tabs-0-tab-2").click()
        GetCodeButton = find_element(self.browser, By.XPATH, "//span[text()='获取验证码']").text
        self.assertEqual(GetCodeButton, "获取验证码")

    def test_loginForgetPwButtonClick(self):
        '''点击忘记密码按钮'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        ForgetPwButtonClick = find_element(self.browser, By.XPATH, "//label[@class='u-default-dot active']").text
        self.assertEqual(ForgetPwButtonClick, "1")

    def test_loginVerifyAccount(self):
        '''忘记密码-验证账号项'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VerifyAccount = find_elements(self.browser, By.XPATH, "//span[@class='u-dot-desc']")[0].text
        self.assertEqual(VerifyAccount, "验证账号")

    def test_loginVAInputBox(self):
        '''验证账号-账号输入框提示'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VAInputBox = find_elements(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']")[0].get_attribute('placeholder')
        self.assertEqual(VAInputBox, "手机号/电子邮箱")

    def test_loginVAGetCodeInputBox(self):
        '''验证账号-验证码输入框提示'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VAGetCodeInputBox = find_element(self.browser, By.XPATH, "//input[@class='ant-input u-input-mid f-fl']").get_attribute('placeholder')
        self.assertEqual(VAGetCodeInputBox, "请输入验证码")

    def test_loginVAGetCodeButton(self):
        '''验证账号-获取验证码按钮'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VAGetCodeButton = find_element(self.browser, By.XPATH, "//span[text()='获取验证码']").text
        self.assertEqual(VAGetCodeButton, "获取验证码")

    def test_loginVANextButton(self):
        '''验证账号-获取验证码按钮'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VANextButton = find_element(self.browser, By.XPATH, "//span[text()='下一步']").text
        self.assertEqual(VANextButton, "下一步")

    def test_loginVAExistingAccountButton(self):
        '''验证账号-获取验证码按钮'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VAExistingAccountButton = find_element(self.browser, By.XPATH, "//span[text()='使用已有账号登录']").text
        self.assertEqual(VAExistingAccountButton, "使用已有账号登录")

    def test_loginVAAccountLack(self):
        '''验证账号-账号缺少提示'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        find_element(self.browser, By.XPATH, "//span[text()='获取验证码']").click()
        VAAccountLack = find_element(self.browser, By.XPATH, "//span[text()='请输入账号']").text
        self.assertEqual(VAAccountLack, "请输入账号")

    def test_loginVAAccountError(self):
        '''验证账号-账号格式错误提示'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        find_element(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']").send_keys(1371266600)
        find_element(self.browser, By.XPATH, "//span[text()='获取验证码']").click()
        VAAccountError = find_element(self.browser, By.XPATH, "//span[text()='账号格式错误']").text
        self.assertEqual(VAAccountError, "账号格式错误")

    def test_loginVAInputVCode(self):
        '''验证账号-请输入验证码提示'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        find_element(self.browser, By.XPATH, "//input[@class='ant-input u-input-big']").send_keys(13712666007)
        find_element(self.browser, By.XPATH, "//span[text()='下一步']").click()
        VAInputVCode = find_element(self.browser, By.XPATH, "//span[text()='请输入验证码']").text
        self.assertEqual(VAInputVCode, "请输入验证码")

    def test_loginVAExistingAL(self):
        '''验证账号-使用已有账号登录'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        find_element(self.browser, By.XPATH, "//span[text()='使用已有账号登录']").click()
        VAExistingAL = find_element(self.browser, By.XPATH, "//div[@id='rc-tabs-1-tab-1']").text
        self.assertEqual(VAExistingAL, "账号密码登录")

    def test_loginVASetPassword(self):
        '''忘记密码-设置密码项'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VASetPassword = find_elements(self.browser, By.XPATH, "//span[@class='u-dot-desc']")[1].text
        self.assertEqual(VASetPassword, "设置密码")

    def test_loginVAChangePassword(self):
        '''忘记密码-修改成功项'''
        self.login()
        find_element(self.browser, By.XPATH, "//span[text()='忘记密码']").click()
        VAChangePassword = find_elements(self.browser, By.XPATH, "//span[@class='u-dot-desc']")[2].text
        self.assertEqual(VAChangePassword, "修改成功")

    def test_loginSuccess(self):
        '''账号密码登录成功'''
        self.login()
        self.test_loginbypw()
        time.sleep(1)
        HomeMenu = find_element(self.browser, By.XPATH, "//a[text()='首页']").text
        self.assertEqual(HomeMenu, "首页")

    def tearDown(self):
        self.log.log_info("登录测试结束")
        time.sleep(3)
        self.driver.tearDown()


if __name__ == '__main__':
    unittest.main()
