from selenium.webdriver.common.by import By

from page.base import Base

class Shop(Base):
    def shop(self):
        # self.driver.find_element_by_class_name('ecsc-search-button').click()
        self.click(By.CLASS_NAME,'ecsc-search-button')
        # self.driver.find_element_by_class_name('p-btn').click()
        self.click(By.CLASS_NAME,'p-btn')
        # #  切换frame
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        # # 验证 打印
        print(self.driver.find_element_by_xpath('//div[@class="conect-title"]/span').text)

    def shop_add(self):
        return self.driver.find_element_by_xpath('//div[@class="conect-title"]/span').text

