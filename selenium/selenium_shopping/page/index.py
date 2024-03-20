# 首页   goto  login    goto  shop
from selenium.webdriver.common.by import By

from page.base import Base
from page.login import Login
from page.shopping import Shop


class Index(Base):
    def goto_login(self):
        self.click(By.LINK_TEXT,'登录')
        return Login(self.driver)
    def goto_shop(self,keyword):
        self.input(By.ID,'q',keyword)
        self.click(By.CLASS_NAME,'ecsc-search-button')
        return Shop(self.driver)
