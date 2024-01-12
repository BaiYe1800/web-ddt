import logging
import time

import allure
import pytest
from webdriver_helper import get_webdriver
from core.pom import LoginPage, UserGoodsFavorPage

logger = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def driver():
    # 未登录的浏览器
    driver = get_webdriver()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def user_driver():
    # 已登录的浏览器
    driver = get_webdriver()
    driver.get(LoginPage.url)
    page = LoginPage(driver)
    page.login("username", "password")
    page.wait_url_change()  # 等待登录完成，页面跳转
    yield driver
    driver.quit()


# 取消收藏
@pytest.fixture(scope='module')
def clear_favor(user_driver):
    # 编写商品收藏页面的pom，进入商品收藏页面，点击删除
    user_driver.get(UserGoodsFavorPage.url)
    user_driver.get_screenshot_as_file()
    page = UserGoodsFavorPage(user_driver)
    page.delete_all()


# 如果用例有什么前置依赖，那应该由夹具来实现


def pytest_runtest_setup(item):
    logger.info(f"开始执行:{item.nodeid}".center(60, "_"))


def pytest_runtest_teardown(item):
    logger.info(f"执行结束:{item.nodeid}".center(60, "_"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    path = f"images/{time.time()}.png"

    if report.when == "call":

        o = report.outcome
        s = f"用例执行结果：【{report.outcome}】"
        if o == "failed":
            logger.error(s)
        elif o == "skip":
            logger.warning(s)
        else:
            logger.info(s)

        if "user_driver" in item.fixturenames:
            driver = item.funcargs['user_driver']
            # driver.get_screenshot_as_file(path)
            # logger.info(f"页面截图：{path}")
            allure.attach(driver.get_screenshot_as_png(), "页面截图")
