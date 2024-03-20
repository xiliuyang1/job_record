# 进入首页  根据功能  组装  新建  goto login   goto free
from selenium.webdriver.common.by import By

from page_feishu.page.basepage import Base
from page_feishu.page.free import Free
from page_feishu.page.login import Login

import time


class Index(Base):
    def goto_login(self):
        self.driver.execute_script('window.scrollTo(0,3000)')
        time.sleep(5)
        # self.driver.find_element_by_link_text('登录')
        self.click(By.LINK_TEXT,'登录')

        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        # self.window(self.driver.window_handles[-1])
        return Login(self.driver)

    def goto_free(self):
        self.driver.find_element_by_link_text('免费使用').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return Free(self.driver)
