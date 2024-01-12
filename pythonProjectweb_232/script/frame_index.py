import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.创建驱动对象(谷歌)
driver = webdriver.Chrome()

# 3.准备一个需要被测url地址
url = "https://mail.qq.com/"

# 4.访问被测试页面
driver.get(url)
# 5.将页面最大化
driver.maximize_window()
# 没有切换框架之前输出主页面的元素文本信息
print(driver.find_element(By.XPATH,'//*[@id="login_pictures"]/div[2]/p[1]').text)
frame1 = driver.find_element(By.XPATH, '//*[@id="QQMailSdkTool_login_loginBox_qq"]/iframe')
driver.switch_to.frame(frame1)
print("----"*100)
# 切换框架之后输出主页面的元素文本信息
# print(driver.find_element(By.XPATH,'//*[@id="login_pictures"]/div[2]/p[1]').text)

frame = driver.find_element(By.XPATH, '//*[@id="ptlogin_iframe"]')
driver.switch_to.frame(frame)
# input("进行调试：")
# 点击账号密码登录
driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys("7891011")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()

time.sleep(5)
driver.quit()
