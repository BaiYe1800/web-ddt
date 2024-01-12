from selenium.webdriver import Chrome, Firefox, Ie, Safari


def get_webdriver(name: str = 'Chrome'):
    # 根据实参，启动特定的浏览器
    # 将实参进行格式化：
    # 英文字符全部转化为小写

    name = name.lower()
    # print(name)
    # 空格去除
    name = name.replace(" ", "")
    # print(name)
    match name:
        case "chrome":
            return Chrome()
        case "firefox":
            return Firefox()
        case "ie":
            return Ie()
        case "safari":
            return Safari()
