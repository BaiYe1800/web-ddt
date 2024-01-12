import json

import requests

import csv


def imgcode(file):
    url2 = 'http://upload.chaojiying.net/Upload/Processing.php'
    data = {
        # 用户名
        'user': 'tianqiu2',
        # 密码：pass（原生密码）和pass2（md5加密32为密码）可选其中一个
        # 'pass': 'ltqiu123456',
        'pass2': 'cdba269f9518d5052a1f827b4491ab8c',
        # 用户的个人id，注册完账号之后并且登录，然后通过个人中心申请
        'sofid': '949627',
        # 验证码的类型
        'codetype': 1902
    }
    files = {"userfile": open(file, "rb")}

    resp = requests.post(url2, data=data, files=files)
    res = resp.json()

    if res['err_no'] == 0:
        code = res['pic_str']
        print(f"识别成功，验证码为：{code}")
    else:
        print("识别失败")
    return code


# 获取cookie信息
def save_cookies(driver):
    # 将获取到的cookie信息保存到本地文件
    cookies = driver.get_cookies()
    with open("cookies.json", "w") as f:
        # python中无法直接使用json数据格式的内容，所以必须进行转化
        # 方法json.dumps()：python数据转化为json数据
        f.write(json.dumps(cookies))


# 使用cookie信息
def load_cookie(driver):
    # 使用cookie信息
    driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
    try:
        with open("cookies.json") as f:
            # 通过json.loads（data）方法把json数据转化为python数据
            cookies = json.loads(f.read())
        for cookie in cookies:
            # 使用页面当中的所有cookie信息
            driver.add_cookie(cookie)
        else:
            # 添加完之后进行清除缓存（刷新页面）
            driver.refresh()
    except:
        print("目前没有可以使用的cookie信息，只能正常登录")


def is_login(driver):
    # 可以通过页面标题判断是否已经登录
    if "管理员登录" in driver.title:
        print("需要进行第一次登录")
        return False
    else:
        print("已登录")
        return True


def get_data_background():
    list1 = []
    c = csv.reader(open(r"D:\pythonProjectweb_232\data\ccssv.csv", "r", encoding="utf8"))

    for cs in c:
        list1.append(cs)
    else:
        return list1


# print(get_data_background())
# import xlrd
#
#
# def func():
#     # 读取Excel表格数据穿件xls表格对象
#     xls = xlrd.open_workbook("D:\pythonProjectweb_232\data\功能测试用例.xlsx")
#     # 通过下标获取表格第一张表
#     sheet = xls.sheet_by_index(0)
#     #
#     # print(sheet.ncols)
#     # print(sheet.nrows)
#     # print(sheet.row_values(1))
#
#     for i in range(sheet.nrows):
#         print(sheet.row_values(i))

#  导包
#  导包
# import logging
# # 定义一个格式化的字符串
# fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
# # 设置日志的级别
# logging.basicConfig(level=logging.DEBUG, format=fmt, filename='../log/a.log')
# # 调用logging输出日志
# logging.debug("这是一条调试级别的日志")
# logging.info("这是一条信息级别的日志")
# logging.warning("这是一条警告级别的日志")
# logging.error("这是一条错误级别的日志")
# logging.critical("这是一条严重级别的日志")


# 2022-1-12 20:33:50 日志级别(文本) 日志名字 调用输出的py文件的名字 函数的名字 行号  输入内容