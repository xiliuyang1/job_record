# 需求 ：1、首页点击登录-点击立即注册
#
# ​			2、首页点击免费使用，输入手机号码‘18888888888’

from selenium import webdriver

import time

class Test:
    # 初始化
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://feishu.cn')
        self.driver.implicitly_wait(3)

    # 首页点击登录-点击立即注册    登录
    def test_login(self):
        self.driver.find_element_by_link_text('登录').click()
        # 获取多窗口
        handles = self.driver.window_handles
        print(handles)
        #  窗口切换
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element_by_xpath('//div[@class="login-go-registe"]/span/span').click()

    # 2、首页点击免费使用，输入手机号码‘18888888888’
    def test_free(self):
        self.driver.find_element_by_link_text('免费使用').click()
        # 窗口切换
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element_by_id('register_phone').send_keys('18888888888')

    # 关闭窗口

    def teardown(self):
        self.driver.quit()