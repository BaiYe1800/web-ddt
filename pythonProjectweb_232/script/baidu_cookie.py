from selenium import webdriver

# 2.创建驱动对象(谷歌)
driver = webdriver.Chrome()

# 3.准备一个需要被测url地址
url = "https://www.baidu.com/"

# 4.访问被测试页面
driver.get(url)

# 5.将页面最大化
driver.maximize_window()

driver.add_cookie({"name": "BAIDUID",
                   "value": "DDC8E5F3435BADE288DF933BF028B014:FG=1"})

driver.add_cookie({"name": "BDUSS",
                   "value": 'BYYUNIUXp5QlZzcGNZZGVWTHZuZ3AwSExFYkwzUXFVSERuNGNwMThOSEFFcWhrSVFBQUFBJCQAAAAAAAAAAAEAAABl3sZssqmwrrKpsK6yqbCu0vkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCFgGTAhYBkQj'})
# 添加完cookie之后一定要刷新缓存
driver.refresh()
input("调试页面：")
driver.quit()
