import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from script.background_logoin import driver

# 需要点击新增贷款之前必须切换子页面frame框架
frame = driver.find_element(By.XPATH, '/html/frameset/frame[1]')
# 切换子页面
driver.switch_to.frame(frame)
# 点击贷款管理
driver.find_element(By.XPATH, '//*[@id="navs"]/ul/li[2]/a').click()
# 重点：注意如果已经切换到子页面，要操作其他子页面或者主页面的元素，那么一定要退出再进入再操作
# 默认切换到主页面
driver.switch_to.default_content()
# 切换新增子页面
time.sleep(1)
frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
driver.switch_to.frame(frame)
# 点击新增按钮
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/input[1]').click()
# 设计新增贷款页面的流程用例
# input("开启调试：")
print("-------" * 100)

# 颜色:
driver.find_element(By.XPATH, '//*[@id="colorpickerField"]').send_keys("f00")
# 借款编号:
el1 = driver.find_element(By.XPATH,
                          '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input')
el1.clear()
el1.send_keys("MER202306099527")
# 贷款名称:
driver.find_element(By.XPATH,
                    '/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input') \
    .send_keys("需要1个小目标：1E")
# 简短名称:
driver.find_element(By.XPATH,
                    '/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input') \
    .send_keys("一个亿")
# 会员名称:
el = driver.find_element(By.XPATH,
                         '/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]')
el.send_keys("beifan")
# 方便选中下拉会员信息，进行强制等待
time.sleep(2)
driver.find_element(By.XPATH,'//strong[text()="beifan"]').click()
# 所在城市:
driver.find_element(By.XPATH,
                    '//*[@id="citys_box"]/div[1]/div[2]/input[3]') \
    .click()
# input("开启调试：")
# 分类:
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select')
select1 = Select(sl1)
select1.select_by_value('4')
# 担保机构:
sl2 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[9]/td[2]/select')
select2 = Select(sl2)
select2.select_by_index(2)
# 担保范围:
sl3 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[10]/td[2]/select')
select3 = Select(sl3)
select3.select_by_visible_text("无")
# input("开启调试：")
# 文件上传
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button').click()
time.sleep(3)
# 点击本地上传
# input("程序开启调试")
# driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div/div[1]/ul/li[2]').click()
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[1]/ul/li[2]').click()
time.sleep(2)                # /html/body/div[5]/div[1]/div[2]/div/div[3]/form/div/div/div/input
# input("程序开启调试")         # /html/body/div[6]/div[1]/div[2]/div/div[3]/form/div/div/div/input
# 手写xpath

driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(r'D:\pythonProjectweb_232\verify.png')
# driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[3]/form/div/div/div/input').send_keys(
#     r'D:\pythonProjectweb_232\verify.png')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[3]/span[1]/input').click()
# input("开启调试：")
# 借款用途
sl4 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select')
select4 = Select(sl4)
select4.select_by_visible_text('婚礼筹备')

# 还款方式
sl5 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[16]/td[2]/select')
select5 = Select(sl5)
select5.select_by_visible_text('付息还本')

# 借款合同范本
sl6 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select')
select6 = Select(sl6)
select6.select_by_visible_text('天天赢合作操盘协议')
# 转让合同范本
sl6 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select')
select6 = Select(sl6)
select6.select_by_visible_text('周周盈合作操盘协议')
# 借款金额
el2 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input')
el2.clear()
el2.send_keys("1000000")

# 借款保证金[第三方托管]:
el3 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input')
el3.clear()
el3.send_keys("200000")
# 投标类型:
sl7 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[21]/td[2]/select')
select7 = Select(sl7)
select7.select_by_visible_text('按金额')
# 最低投标金额:

el4 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[22]/td[2]/input')
el4.clear()
el4.send_keys("100")
# driver.find_element(By.NAME, 'guarantees_amt').send_keys("100")
# 最高投标金额:
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[23]/td[2]/input').send_keys("100000")
# driver.find_element(By.NAME, 'max_loan_money').send_keys("100000")

# 借款期限:
driver.find_element(By.XPATH, '//*[@id="repay_time"]').send_keys("12")
# 年利率:
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[27]/td[2]/input').send_keys("4")

# 筹标期限:
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input').send_keys("28")
# 可否使用红包:使用默认值
# input("开启调试：")


frame = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[30]/td[2]/div/div/div[2]/iframe')
# 切换子页面
driver.switch_to.frame(frame)
# 输入贷款描述内容
driver.find_element(By.XPATH, '/html/body').send_keys("急需贷款100万，娶老婆，在线等，很急")

# 默认切换到主页面
driver.switch_to.default_content()

# 风险等级:使用默认值

# 风险控制
# 先切换整个输入子页面
frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
driver.switch_to.frame(frame)
# 再切换输入具体内容的风险信息子页面
frame = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[32]/td[2]/div/div/div[2]/iframe')
# 切换子页面
driver.switch_to.frame(frame)
# 输入分线控制的描述信息
driver.find_element(By.XPATH, '/html/body').send_keys("没有任何的风险，放心借")
# 默认切换到主页面
driver.switch_to.default_content()
# input("开启调试：")
# 需要进行页面切换才能点击状态：
frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
driver.switch_to.frame(frame)
# 借款状态:
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]').click()

# 开始时间:
# 可以通过开发者工具进行强制输入时间：
# 通过控制台的xpath进行具体值的输入：
# $x('//*[@id="start_time"]')[0].value='2023-06-23 21:30:14'
driver.implicitly_wait(3)
# 当元素不可交互，不是因为前置触发条件造成的，那么就可以使用JavaScript脚本进行强制输入
# 需要在页面中定义一个JavaScript脚本来接收实际强制输入参数信息
# function add_time(params) {
# console.log(arguments[0])
# }
el5 = driver.find_element(By.XPATH, '//*[@id="start_time"]')
# 通过JavaScript脚本执行实际参数的输入
driver.execute_script('"arguments[0].value="2023-06-12 21:56:58"', el5)

# 排序:默认
# 新增按钮
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]').click()
input("开启调试：")
