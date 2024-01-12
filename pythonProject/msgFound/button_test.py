import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pytest


# 测试用例
def atest_explicit_wait_and_click():
    driver = webdriver.Chrome()
    driver.get('https://35win.info/')  # 替换为目标网站的 URL

    # 点击其他元素
    # driver.find_element(By.XPATH, '//*[@id="app"]/form/div[5]/div/button').click()  # 替换为其他需要点击的元素的 ID
    # 等待目标元素出现
    wait = WebDriverWait(driver, 10)


    # 循环点击其他按钮
    for i in range(3):  # 替换为需要点击的按钮的次数
        other_button = driver.find_element(By.XPATH, '//*[@id="app"]/form/div[5]/div/button')  # 替换为其他按钮的 ID 或其他定位方式
        ActionChains(driver).move_to_element(other_button).click().perform()
    element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/p')))
    print(element.text)