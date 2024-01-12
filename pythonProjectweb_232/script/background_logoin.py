import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from commons.utils import imgcode, save_cookies, load_cookie, is_login

# 2.创建驱动对象(谷歌)
driver = webdriver.Chrome()

# 3.准备一个需要被测url地址
url = "http://47.107.116.139/fangwei/m.php?m=Public&a=login&"

# 4.访问被测试页面
driver.get(url)

# 5.将页面最大化
driver.maximize_window()
# 使用cookie信息
load_cookie(driver)

# 设计用例脚本
if not is_login(driver):
    # 输入账号
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input').send_keys(
        "admin")
    # 输入密码
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input').send_keys(
        "msjy123")
    # 输入验证码
    # 1.截图获取验证码图片
    driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot('verify.png')
    # 发送验证码图片给第三方打码平台
    code = imgcode()
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input').send_keys(code)
    # 点击登录按钮
    driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()
    # 登录完之后保存的cookie信息
    save_cookies(driver)

    time.sleep(5)
    # 6.关闭驱动对象
    driver.quit()
