# # import openpyxl
# #
# # # 打开Excel表格
# # workbook = openpyxl.load_workbook(r'D:\pythonProjectweb_232\data\666.xlsx')
# #
# # # 打开表格的具体工作簿
# # sheet = workbook.active  # active默认代表第一张工作簿
# # # 工作簿的切换通过workbook["工作簿名字"]
# # sheet2 = workbook["Sheet2"]
# #
# # # 通过迭代遍历工作簿中的所有内容
# # for row in sheet2.iter_rows(values_only=True):
# #     print(row)
# #
# # # A1 = sheet['A1']
# # # # print(A1)
# # # a1 = sheet.cell(1, 1)
# # # print(a1)
# # # a1.value = "标记"
# #
# # # workbook.save("test_tianqiu.xlsx")
# from data.files import ExcelFile
#
# # Excel数据类处理工作簿
#
#
# excel = ExcelFile(r"D:\pythonProjectweb_232\data\666.xlsx")
#
# print(excel)
# # {'Sheet1': [('标记', '内容'), ('name', 'web自动化测试'), ('lib', 'selenium'), ('name', 'api自动化测试'), ('lib', 'requests'), ('name', 'app自动化测试'), ('lib', 'appium')],
# # 'Sheet2': [(1, 2, 3), (1, 2, 3), (1, 2, 3)],
# # 'Sheet3': [('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c')]}

#
# def func(num: str | None = 0):
#     print(num)
# func()
