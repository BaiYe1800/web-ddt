import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.创建驱动对象(谷歌)
driver = webdriver.Chrome()

# 3.准备一个需要被测url地址
url = "http://47.107.116.139/fangwei/"

# 4.访问被测试页面
driver.get(url)

# 5.将页面最大化
driver.maximize_window()

# 进行登录成功用例脚本设计
# - 点击登录按钮
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/a').click()
# - 账号密码输入
# 账号
# input("进行调试：")
# 一般如果元素交互，有页面提示或者页面跳转
# 会进行强制等待（隐式等待，显示等待）
time.sleep(1)
# 账号
driver.find_element(By.XPATH, '//*[@id="login-email-address"]').send_keys("admin")
# 密码
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys("msjy123")


# - 点击登录按钮
driver.find_element(By.XPATH, '//*[@id="ajax-login-submit"]').click()

# - 进行登录成功之后断言
time.sleep(1)
msg = driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
print(msg)
assert msg == "成功登录"

# - 登录成功之后点击提示按钮（确定）
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()




# 进行投标成功的用例脚本设计
# - 点击马上投标
driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[1]/span[6]/a/span').click()

# - 输入投标金额
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="J_BIDMONEY"]').send_keys("100000")

# - 点击立即投资
time.sleep(1)
# input("进行调试：")
driver.find_element(By.XPATH,'//*[@id="tz_link"]').click()
                            # //*[@id="tz_link"]
                            # //*[@id="tz_link"]
# - 输入支付密码
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="J_bid_password"]').send_keys('msjy123')

# - 点击确定投标按钮
driver.find_element(By.XPATH,'//*[@id="J_bindpassword_btn"]').click()


# 获取实际结果进行断言
time.sleep(1)
msg2 = driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
print(msg2)
assert msg2 == "投标成功！"

# - 提示信息的确定按钮关闭
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()



input("进行调试：")





# 关闭驱动
driver.quit()
