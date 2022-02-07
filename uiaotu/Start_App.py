from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'how10', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.taobao.taobao', # 启动APP Package名称
  'appActivity': 'com.taobao.tao.welcome.Welcome', # 启动Activity名称
  # 'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  # 'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  # 'newCommandTimeout': 6000,
  # 'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
def starapp():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

