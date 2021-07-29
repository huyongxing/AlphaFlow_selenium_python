#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# @Author  : huyx
# @Time    : 2021/7/16 15:16
# @Software: PyCharm

from test_case.suite import *


def suite():
    suite = unittest.TestSuite()
    suite.addTest(login_case.Login_Case("test_loginAccountPwMenu"))
    suite.addTest(login_case.Login_Case("test_loginAccountInputBox"))
    suite.addTest(login_case.Login_Case("test_loginPwInputBox"))
    suite.addTest(login_case.Login_Case("test_loginBotton"))
    suite.addTest(login_case.Login_Case("test_loginOtherWays"))
    suite.addTest(login_case.Login_Case("test_loginForgetPw"))
    suite.addTest(login_case.Login_Case("test_loginAccountLack"))
    suite.addTest(login_case.Login_Case("test_loginAccountError"))
    suite.addTest(login_case.Login_Case("test_loginPwLack"))
    suite.addTest(login_case.Login_Case("test_loginPwError"))
    suite.addTest(login_case.Login_Case("test_loginVerificaCode"))
    suite.addTest(login_case.Login_Case("test_loginVCAccountInputBox"))
    suite.addTest(login_case.Login_Case("test_loginVCodeInputBox"))
    suite.addTest(login_case.Login_Case("test_loginGetCodeButton"))
    suite.addTest(login_case.Login_Case("test_loginForgetPwButtonClick"))
    suite.addTest(login_case.Login_Case("test_loginVerifyAccount"))
    suite.addTest(login_case.Login_Case("test_loginVAInputBox"))
    suite.addTest(login_case.Login_Case("test_loginVAGetCodeInputBox"))
    suite.addTest(login_case.Login_Case("test_loginVAGetCodeButton"))
    suite.addTest(login_case.Login_Case("test_loginVANextButton"))
    suite.addTest(login_case.Login_Case("test_loginVAExistingAccountButton"))
    suite.addTest(login_case.Login_Case("test_loginVAAccountLack"))
    suite.addTest(login_case.Login_Case("test_loginVAAccountError"))
    suite.addTest(login_case.Login_Case("test_loginVAInputVCode"))
    suite.addTest(login_case.Login_Case("test_loginVAExistingAL"))
    suite.addTest(login_case.Login_Case("test_loginVASetPassword"))
    suite.addTest(login_case.Login_Case("test_loginVAChangePassword"))
    suite.addTest(login_case.Login_Case("test_loginSuccess"))

    return suite
