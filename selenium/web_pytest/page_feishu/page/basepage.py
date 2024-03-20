from selenium import webdriver

import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

'''basepage是所有pageobject的父类，  为子类提供公共方法， 比如初始化 driver 和退出driver
代码在base_page模块的basepage类使用——init——初始方法进行初始化操作，包括driver的复用
driver的赋值、全局的等待时间设置 == 常见隐式等待'''

# 创建base基类
from selenium import webdriver

from selenium.webdriver.remote.webdriver import WebDriver
import time
# webdriver 定义  标识说明



class Base:

    def __init__(self, driver: WebDriver = None):
        # 传入数据 driver 以及driver 初始化 做对应的判断
        if driver is None:  # 此处对driver进行复用，如果不存在driver，就构造一个新的
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.get('https://www.feishu.cn/')

        else:  # 如果driver有值，比如login 和 free 页面需要这个方法，避免重复构造driver
            self.driver = driver


    def close(self):
        time.sleep(5)
        self.driver.quit()

    # 提取find方法
    def find(self,by,loc):
        return WebDriverWait(self.driver,timeout=6).until(lambda x :self.driver.find_element(by,loc))

    # 提取click方法
    def click(self,by,loc):
        return self.find(by,loc).click()
    # 提取输入方法

    def keys(self,by,loc,v):
        return self.find(by,loc).send_keys(v)


    # 提取text
    def text(self,by,loc):
        return self.find(by,loc).text

    # 提取 window
    def window(self,window_name):
        return self.driver.switch_to.window(window_name)


