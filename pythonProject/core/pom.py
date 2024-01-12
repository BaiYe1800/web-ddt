from webdriver_helper.pom import *


class LoginPage(BasePage):
    url = "https://www.baidu.com"
    ipt_username = LazyElement(By.XPATH, '****')
    ipt_password = LazyElement(By.XPATH, '****')
    btn_submit = LazyElement(By.XPATH, '****')
    p_msg = LazyElement(By.XPATH, '****', check_on_init=False)  # 动态元素，初始化不检查是否存在

    def get_msg(self):
        return self.wait.until(lambda _: self.p_msg.text)

    def login(self, username, password):
        self.send_keys(self.ipt_username, username)
        self.send_keys(self.ipt_password, password)
        self.click(self.btn_submit)


class UserPage(BasePage):
    url = "https://www.baidu.com/user"
    ipt_username = LazyElement(By.XPATH, '****')
    ipt_password = LazyElement(By.XPATH, '****')
    btn_submit = LazyElement(By.XPATH, '****')
    p_msg = LazyElement(By.XPATH, '****', check_on_init=False)  # 动态元素，初始化不检查是否存在

    def get_msg(self):
        return self.wait.until(lambda _: self.p_msg.text)

    def login(self, username, password):
        self.send_keys(self.ipt_username, username)
        self.send_keys(self.ipt_password, password)
        self.click(self.btn_submit)


class UserGoodsFavorPage(BasePage):
    url = "https://www.baidu.com/user/2"
    btn_check = LazyElement(By.XPATH, '****')
    btn_delete = LazyElement(By.XPATH, '****')
    btn_confirm = LazyElement(By.XPATH, '//div/span[text()="确定“]', check_on_init=False)

    def get_msg(self):
        return self.wait.until(lambda _: self.p_msg.text)

    def delete_all(self):
        if self.btn_check.is_enabled():  # 如果按钮可以点击
            self.click(self.btn_check)
            self.click(self.btn_delete)
            self.click(self.btn_confirm)
            return self.get_msg()
