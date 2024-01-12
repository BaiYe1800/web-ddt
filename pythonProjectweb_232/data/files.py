import openpyxl
import yaml


class YamlFile(dict):
    def __init__(self, path):
        super().__init__()  # 让对象接照原来方完成实例化
        # 接下来完成自定义的代码
        self._path = path  # yaml文件路径
        self.load()  # 实例化时，自动加载yaml内容

    def load(self):
        with open(self._path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)  # 字典
        if data:
            self.update(data)  # 两个字典内容进行合#

    def save(self):
        with open(self._path, "w", encoding="utf-8") as f:
            yaml.dump(dict(self), f, allow_unicode=True)


class ExcelFile(YamlFile):
    def load(self):
        # 打开Excel表格
        workbook = openpyxl.load_workbook(self._path)
        data = {}
        for sheet in workbook.worksheets:  # 迭代每一张工作簿
            data[sheet.title] = []  # 每个工作簿都是一个k（工作簿的名字）-v（工作簿的所有值）
            for row in sheet.iter_rows(values_only=True):
                # print(row) # 打印所有工作簿的实际数据内容
                data[sheet.title].append(row)
        if data:
            self.update(data)  # 两个字典内容进行合
