import os

import pytest

pytest.main()

# pytest 运行完毕之后，开始生成报告
os.system("allure serve .allure_results")
