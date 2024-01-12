# 封装前台登录页面类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func（形参） = f(实参)
        return WebDriverWait(self.driver, 5).until(func)

    # 在页面类当中重写定位元素的方法并且结合显示等待一起使用
    def find_element(self, by, value, need_wait=False):
        def f(driver):
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


class ReceptionLoginPage(BasePage):
    # 页面中需要被操作的元素全部定义成类属性
    # 登录按钮元素
    btn_login = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/a')
    # 账号
    ipt_username = (By.XPATH, '//*[@id="login-email-address"]')
    # 密码
    ipt_password = (By.XPATH, '//*[@id="login-password"]')
    # 点击登录按钮
    btn_login_submit = (By.XPATH, '//*[@id="ajax-login-submit"]')
    # 获取登录的提示信息:登录成功和失败定位元素xpath值也不一样
    # // *[ @ id = "fanwe_error_box"] / table / tbody / tr / td[2] / div[2]
    txt_login_msg = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]')
    # 登录成功之后的确定按钮
    btn_login_ok = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]')
    # - 点击马上投标
    btn_deal_submit = (By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[2]/span[6]/a/span')
    # - 输入投标金额              # /html/body/div[7]/div[2]/div[1]/div[1]/ul/li[2]/span[6]/a/span
    ipt_money = (By.XPATH, '//*[@id="J_BIDMONEY"]')
    # - 点击立即投资
    btn_deal_submit2 = (By.XPATH, '//*[@id="tz_link"]')
    # - 输入支付密码
    ipt_pay_password = (By.XPATH, '//*[@id="J_bid_password"]')
    # - 点击确定投标按钮
    btn_pay_submit = (By.XPATH, '//*[@id="J_bindpassword_btn"]')
    # - 提示信息的确定按钮关闭
    txt_deal_msg = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[2]')

    # 反例的提示信息的xpath
    # //*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]
    def login(self, username, password):
        # 点击登录按钮
        # *self.btn_login:通过对象本身调用类属性
        self.find_element(*self.btn_login).click()

        self.find_element(*self.ipt_username, need_wait=True)
        # 输入账号
        self.find_element(*self.ipt_username).send_keys(username)
        # 输入密码
        self.find_element(*self.ipt_password).send_keys(password)
        # 点击确定登录按钮
        self.find_element(*self.btn_login_submit).click()
        # 触发显示等待
        self.find_element(*self.btn_login_ok, need_wait=True)
        # 获取实际结果文本信息
        msg = self.find_element(*self.txt_login_msg, need_wait=True).text
        # 点击确定关闭登录按钮
        self.find_element(*self.btn_login_ok).click()

        return msg

    def pay(self, money, password):
        # 点击马上投标
        # self.find_element(*self.btn_deal_submit).click()
        # - 输入投标金额
        self.find_element(*self.ipt_money).send_keys(money)
        # - 点击立即投资
        self.find_element(*self.btn_deal_submit2).click()
        # - 输入支付密码
        self.find_element(*self.ipt_pay_password).send_keys(password)
        # - 点击确定投标按钮
        self.find_element(*self.btn_pay_submit).click()
        # - 提示信息的实际结果
        msg = self.find_element(*self.txt_deal_msg, need_wait=True).text
        # 关闭确定按钮
        self.find_element(*self.txt_deal_msg).click()
        return msg


class BackGroundLoginPage(BasePage):
    # 账号
    ipt_username = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
    # 密码
    ipt_password = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
    # 验证码图片
    code_png = (By.XPATH, '//*[@id="verify"]')
    # 输入验证码
    ipt_code = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
    # 点击登录按钮
    btn_login_submit = (By.XPATH, '//*[@id="login_btn"]')
    # 获取实际结果
    txt_login_msg = (By.XPATH, '//*[@id="login_msg"]')

    def login(self, username, password, code):
        """执行用例的所有操作并且使用类属性（需要被操作的元素）"""
        # 输入账号
        self.find_element(*self.ipt_username).send_keys(username)
        # 输入密码
        self.find_element(*self.ipt_password).send_keys(password)
        # 验证码图片
        # self.find_element(*self.code_png).screenshot('verify.png')
        # driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot('verify.png')
        # 输入验证码
        self.find_element(*self.ipt_code).send_keys(code)
        # 点击登录
        self.find_element(*self.btn_login_submit).click()
        # 获取实际结果
        msg = self.find_element(*self.txt_login_msg, need_wait=True).text
        return msg

    # 截图验证码图片
    def save_img(self, path):
        el1 = self.find_element(*self.code_png)
        el1.screenshot(path)


class A(BasePage):
    pass


class B(BasePage):
    pass


class C(BasePage):
    pass


class D(BasePage):
    pass
