import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver :WebDriver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('http://www.localhost:8081')
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver

# 查找元素

    def find(self,by,loc):
        return WebDriverWait(self.driver,timeout=30).until(lambda x:self.driver.find_element(by,loc))

# 点击方法

    def click(self,by,loc):
        return self.find(by,loc).click()

# 输入方法
    def input(self,by,loc,v):
        return self.find(by,loc).send_keys(v)

# 获取文本信息

    def text(self,by,loc):
        return self.find(by,loc).text

# 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime("%Y_%m_%d_%H_%M_%S")))

# 判断元素是否存在

    def base_element_is_exist(self,loc):
        try:
            self.find(loc)
            return True
        except:
            return False

