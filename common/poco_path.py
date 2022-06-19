import os

# 获取项目所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 环境开关路径
GLOBAL_FILE = os.path.join(BASE_DIR, "config", 'global.conf')

# 测试报告所在的目录路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")
# 日志文件所在的目录路径
LOG_DIR = os.path.join(BASE_DIR, "outputs", "logs")
# 测试结果截图
SCREENSHOT_DIR = os.path.join(BASE_DIR, "outputs", "screenshots")



# 用例脚本所在的目录路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")  # 所有用例
DAILY_DIR = os.path.join(BASE_DIR, "testcases", "test_openapi")  # open_api
DAILY_C2_DIR = os.path.join(BASE_DIR, "testcases", "test_c2")  # clink2


# 所有用例数据所在的目录路径
DATA_DIR = os.path.join(BASE_DIR, "data")
# 发布回归用例数据所在的目录路径
DAILY_DIR_DATA = os.path.join(BASE_DIR, "data", "daily")
DAILY_C2_DIR_DATA = os.path.join(BASE_DIR, "data", "daily_c2")

if __name__ == '__main__':
    print(GLOBAL_FILE)
