# 使用页面类中的属性执行用例脚本
import time

import pytest
from selenium.webdriver.common.by import By

from commons.kdt import KeyWord
from commons.pom import ReceptionLoginPage, BackGroundLoginPage


# 支付流程用例的正例
@pytest.mark.skip
def test_user_deal_ok(user_driver, clear_deal_page):
    page = ReceptionLoginPage(user_driver)
    msg = page.pay(1000, "msjy123")
    print(msg)
    assert msg == "投标成功！"


@pytest.mark.skip
def test_user_deal_ok2(user_driver, clear_deal_page):
    page = ReceptionLoginPage(user_driver)
    msg = page.pay(1000, "msjy123")
    print(msg)
    assert msg == "投标成功！"


# 支付流程用例的反例
@pytest.mark.skip
def test_user_deal_fail(user_driver, clear_deal_page):
    page = ReceptionLoginPage(user_driver)

    msg = page.pay(10000, "msjy123456789")
    print(msg)
    assert msg == "支付密码错误"


# 通过关键字实现前台登录功能
def test_user_login_fail_by_kdt(anonymous_driver):
    anonymous_driver.get('http://47.107.116.139/fangwei/')
    wd = KeyWord(anonymous_driver)
    wd.click('/html/body/div[2]/div/div[2]/div[1]/div/a')
    wd.input('//*[@id="login-email-address"]', "admin")
    wd.input('//*[@id="login-password"]', "13131314")
    wd.click('//*[@id="ajax-login-submit"]')
    wd.assert_text('//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]', '密码错误')
    # msg = wd.get_text('//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]')
    # assert msg == "密码错误"
