import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class KeyWord:
    def __init__(self, driver, *args):
        self.driver = driver

    def wait(self, func, *args):  # func（形参） = f(实参)
        return WebDriverWait(self.driver, 5).until(func)

    # 在页面类当中重写定位元素的方法并且结合显示等待一起使用
    def find_element(self, by, value, need_wait=False, *args):
        def f(driver, *args):
            if driver.find_element(by, value).text:

                msg = driver.find_element(by, value).text
                if need_wait:  # 如果有实际结果文本信息
                    # 当元素存在，但是没有任何内容时，需要进行空值替换，直到有内容获取返回
                    return msg.replace(" ", "")
                else:
                    return True  # 直接成功（没有获取实际结果的内容直接定位元素）
            else:
                return True

        self.wait(f)  # 通过self对象，调用类方法出发显式等待
        return self.driver.find_element(by, value)  # 通过selenium本身元素定位方法进行等待完毕之后再定位

    # 在关键字类中添加关键字
    # loc:str:loc形参指定类型是字符串，接收实参的元素值
    # 点击关键字封装
    def click(self, loc: str, *args):
        el = self.find_element(By.XPATH, loc)
        el.click()

    # 输入关键字封装
    def input(self, loc: str, content="", *args):
        el = self.find_element(By.XPATH, loc)
        el.send_keys(content)

    # 获取实际结果关键字
    def get_text(self, loc: str, need_text=True, *args):

        def f(x, *args):
            e = self.driver.find_element(By.XPATH, loc)
            t = e.text.replace(" ", "")
            if t:  # 文本是否包含非空字符
                return t
            else:
                return False

        if need_text:
            text = self.wait(f)
        else:
            text = self.find_element(By.XPATH, loc).text

        return text

    # 封装断言关键字
    def assert_text(self, loc: str, text: str, *args):
        el_text = self.get_text(loc)  # 页面中的文本实际结果提示信息
        assert el_text == text

    # 封装新增贷款页面关键字
    # 进入
    def frame_enter(self, loc: str, *args):
        el = self.find_element(By.XPATH, loc)
        self.driver.switch_to.frame(el)

    # 退出
    def frame_exit(self, *args):
        self.driver.switch_to.default_content()

    # 清除
    def clear(self, loc: str, *args):
        el = self.find_element(By.XPATH, loc)
        el.clear()

    # 强制等待
    def sleep(self, x, *args):
        time.sleep(x)

    # 选择框
    def select(self, loc: str, text, *args):
        select = Select(self.driver.find_element(By.XPATH, loc))
        select.select_by_visible_text(text)  # 通过文本选择下拉框选项

    # 强制输入时间
    def js(self, loc: str, code, *args):
        el = self.find_element(By.XPATH, loc)
        self.driver.execute_script(code, el)

    # def assert_value(self, loc: str, value: str,*args):
    #     el = self.find_element(By.XPATH, loc)  # 页面中的文本实际结果提示信息
    #     el_value = el.get_attribute('value')
    #     assert el_value == value

    def switch_to_alert(self, text: str, *args):

        alert1 = self.driver.switch_to.alert
        # print(alert1.text)  # 请填写年利率
        assert text == alert1.text
        alert1.dismiss()

    def get(self, url, *args):
        self.driver.get(url)
