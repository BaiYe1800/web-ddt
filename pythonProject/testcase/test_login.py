import pytest

from core.pom import LoginPage, UserPage
from core.data import read_csv
from webdriver_helper import get_webdriver


@pytest.mark.parametrize(
    "username, password, msg",
    read_csv("ddt_test_login.csv"),
)
def test_login(driver, username, password, msg):
    driver.get(LoginPage.url)
    page = LoginPage.login(driver)
    page.login(username, password)
    assert msg == page.get_msg()


def test_adduser(driver, clear_favor):
    driver.get(UserPage.url)
    page = UserPage.login()
    page.login("username", "password")
    msg = page.get_msg()
    assert msg == "登陆成功"


def test_user_new_address(user_driver):
    user_driver.get(UserPage.url)
    page = UserPage(user_driver)
    # page = page.new_address()
    # page.sbmint(
    # "username", "phone", "省时区", alias=""
    # )
    # assert pasge_msg == "操作成功"