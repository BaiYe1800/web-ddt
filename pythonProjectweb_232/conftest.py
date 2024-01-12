import logging

from selenium.webdriver import Chrome

import pytest

from commons.driver import get_webdriver
from commons.kdt import KeyWord

from commons.pom import ReceptionLoginPage, BackGroundLoginPage
from commons.utils import load_cookie, is_login, imgcode, save_cookies
from pytest_xlsx.file import XlsxItem


# 当Excel用例被执行的时候会自动调用
def pytest_xlsx_run_step(item: XlsxItem):
    # 1.实例化关键字对象
    print(item.usefixtures.keys())
    driver_name = list(item.usefixtures.keys())[0]
    driver = item.usefixtures[driver_name]
    wd = KeyWord(driver)
    # 2.获取用例的执行步骤
    step = item.current_step
    # 3.解析关键字和参数信息(通过字典的键值对获取内容)
    key = step["标记"]  # 关键字
    args = [step["内容"], step["列1"]]  # 实际参数信息值

    # 去除空值None
    if args[-1] is None:
        # 删除最后的None空值,pop方法默认删除列表最后一个元素
        args.pop()
    logging.warning(f"关键字= {key},关键字的参数信息{args}")
    # 如果关键字没有任何实参，那么需要对None进行处理
    if key is None:
        return
    # 4.调用关键字和使用关键字参数信息
    func = getattr(wd, key)
    func(*args)
    # wd.sleep(5)


# 匿名驱动
@pytest.fixture
def anonymous_driver():
    driver = get_webdriver()
    yield driver
    driver.quit()


# 前台登录页面的前置驱动
@pytest.fixture(scope='session')
def user_driver():
    driver = get_webdriver()

    driver.get("http://47.107.116.139/fangwei")

    driver.maximize_window()
    # 创建页面对象
    page = ReceptionLoginPage(driver)
    # 通过页面对象执行用例脚本
    msg = page.login("admin", "msjy123")
    # 断言实际结果
    assert msg == "成功登录"
    yield driver


# 后台登录页面的前置驱动
@pytest.fixture(scope="session")
def admin_driver():
    driver = get_webdriver()
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
    # 使用cookie信息
    load_cookie(driver)

    if not is_login(driver):
        # 实例一个后台登录页面的流程用例对象
        page = BackGroundLoginPage(driver)
        # 验证码识别
        page.save_img('code.png')
        code = imgcode('code.png')
        msg = page.login("admin", 'msjy123', code)
        assert msg == "登录成功"

    yield driver
    # 保存cookie信息
    save_cookies(driver)


@pytest.fixture
def clear_deal_page(user_driver):
    user_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24315')
