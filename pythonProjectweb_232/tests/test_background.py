import time

import allure
import pytest
from selenium.webdriver.common.by import By

from commons.kdt import KeyWord
from commons.pom import BackGroundLoginPage
from commons.utils import get_data_background


# @pytest.mark.parametrize("username, password, code,assert_msg", [
#     ["", "", "", "管理员帐号不能为空"],
#     ["admin", "", "", "管理员密码不能为空"],
#     ["admin", "msjy123", "", "验证码不能为空"],
#     ["admin", "msjy123", "6666", "验证码错误"],
#     ["admin2", "msjy123", "6666", "验证码错误"],
# ])
# def test_admin(anonymous_driver, username, password, code, assert_msg):
#     anonymous_driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
#
#     anonymous_driver.maximize_window()
#
#     page = BackGroundLoginPage(anonymous_driver)
#     msg = page.login(username, password, code)
#     print(msg)
#     assert msg == assert_msg
# @allure.step(title="测试登录页面第一步参数化001")
# @pytest.mark.parametrize("username, password, code,assert_msg", get_data_background())
# @allure.step(title="测试登录页面第一步参数化002")
# def test_admin(anonymous_driver, username, password, code, assert_msg):
#     anonymous_driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
#
#     anonymous_driver.maximize_window()
#
#     page = BackGroundLoginPage(anonymous_driver)
#     msg = page.login(username, password, code)
#     print(msg)
#     assert msg == assert_msg


# @pytest.mark.parametrize("username, password, code,assert_msg", [
#     ["", "", "", "管理员帐号不能为空"],
#     ["admin", "", "", "管理员密码不能为空"],
#     ["admin", "msjy123", "", "验证码不能为空"],
#     ["admin", "msjy123", "6666", "验证码错误"],
#     ["admin2", "msjy123", "6666", "验证码错误"],
# ])
# def test_admin_login_by_kdt(anonymous_driver, username, password, code, assert_msg):
#     anonymous_driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
#     anonymous_driver.maximize_window()
#     wd = KeyWord(anonymous_driver)
#     wd.input('/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input', username)
#     wd.input('/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input', password)
#     wd.input('/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input', code)
#     wd.click('//*[@id="login_btn"]')
#
#     msg = wd.get_text('//*[@id="login_msg"]')
#     assert msg == assert_msg

def test_admin_new_deal_by_kdt(admin_driver):
    wd = KeyWord(admin_driver)
    # 点击贷款管理
    wd.frame_enter('/html/frameset/frame[1]')
    wd.click('//*[@id="navs"]/ul/li[2]/a')
    wd.frame_exit()

    # 点击新增按钮
    wd.frame_enter('//*[@id="main-frame"]')
    wd.click('/html/body/div[2]/div[3]/input[1]')

    # 输入内容
    # 颜色
    wd.input('//*[@id="colorpickerField"]', "f00")
    # 借款编号:
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input', "MER202306099527")
    # # 贷款名称:
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input', "需要1个小目标：1E")
    # # 简短名称:
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input', "一个亿")
    # 会员名称:
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]', "beifan")
    # 强制等待
    wd.sleep(2)
    wd.click('//strong[text()="beifan"]')
    # 所在城市:
    wd.click('//*[@id="citys_box"]/div[1]/div[2]/input[3]')

    # input("开启调试：")
    # 分类:
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select', '|--信用认证标')
    # 担保机构
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[9]/td[2]/select', "担保机构01")
    # 担保范围
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[10]/td[2]/select', "无")
    # 文件上传
    wd.click('/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button')
    wd.click('/html/body/div[6]/div[1]/div[2]/div/div[1]/ul/li[2]')
    wd.input('//input[@type="file"]', r'D:\pythonProjectweb_232\code.png')
    wd.click('/html/body/div[6]/div[1]/div[3]/span[1]/input')
    # 借款用途
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select', '个人消费')

    # 还款方式
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[16]/td[2]/select', '到期还本息')
    # 借款合同范本
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select', '付息还本合同范本【担保】')
    # 转让合同范本
    wd.select('/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select', '天天赢合作操盘协议')
    # 借款金额
    wd.clear('/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input')
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input', '500000')
    # 借款保证金[第三方托管]:
    wd.clear('/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input')
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input', '200000')
    #  最低投标金额:
    wd.clear('/html/body/div[2]/form/table[1]/tbody/tr[22]/td[2]/input')
    wd.input('/html/body/div[2]/form/table[1]/tbody/tr[22]/td[2]/input', '100')
    # frame子页面切换
    wd.frame_enter('/html/body/div[2]/form/table[1]/tbody/tr[30]/td[2]/div/div/div[2]/iframe')
    wd.input("/html/body", "66666666666666666666")
    wd.frame_exit()

    wd.frame_enter('//*[@id="main-frame"]')
    wd.input("/html/body", "7777777")

    # 强制输入数据
    wd.click('/html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]')
    wd.js('//*[@id="start_time"]', "arguments[0].value='2023-06-12 21:56:58'")

    # 新增
    wd.click('/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]')
    wd.sleep(2)


    wd.switch_to_alert("请填写年利率")
    wd.sleep(3)



