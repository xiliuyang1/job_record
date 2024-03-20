from selenium import webdriver

import time


class Test:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8081')
        self.driver.implicitly_wait(5)


    def test_login_pass(self):
        # sbtbutton   verify_code
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('username').send_keys('18888888888')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_name('sbtbutton').click()
        # 获取提示信息   进行断言
        msg = self.driver.find_element_by_class_name('mu-m-phone').text
        assert msg == '18888888888',"断言提示信息，预期结果【18888888888】，实际结果【%s】"%msg
        print('登录成功')



















    # 账号不存在   layui-layer-content

    # def test_account_not_exist(self):
    #     self.driver.find_element_by_link_text('登录').click()
    #     self.driver.find_element_by_id('username').send_keys('18888888889')
    #     self.driver.find_element_by_id('password').send_keys('123456')
    #     self.driver.find_element_by_id('verify_code').send_keys('8888')
    #     self.driver.find_element_by_name('sbtbutton').click()
    #     # class  定位   属性中间的空格并不是空字符串，间隔符号，class属性名称多个，我们可以取其中一个属性，前提确保重复，
    #     # css    .layui-layer-content.layui-layer-padding
    #     msg = self.driver.find_element_by_class_name('layui-layer-content').text
    #     assert msg == '账号不存在!', "断言提示信息，预期结果【账号不存在!】，实际结果【%s】"%msg
    #     print('提示信息验证通过')
    #
    # #  密码错误
    # def test_error_password(self):
    #     self.driver.find_element_by_link_text('登录').click()
    #     self.driver.find_element_by_id('username').send_keys('18888888888')
    #     self.driver.find_element_by_id('password').send_keys('12345')
    #     self.driver.find_element_by_id('verify_code').send_keys('8888')
    #     self.driver.find_element_by_name('sbtbutton').click()
    #     # class  定位   属性中间的空格并不是空字符串，间隔符号，class属性名称多个，我们可以取其中一个属性，前提确保重复，
    #     # css    .layui-layer-content.layui-layer-padding
    #     msg = self.driver.find_element_by_class_name('layui-layer-content').text
    #     assert msg == '密码错误!', "断言提示信息，预期结果【密码错误!】，实际结果【%s】"%msg
    #     print('提示信息验证通过')
    #
    # # 购物车   提示信息  添加成功       搜索按钮 ecsc-search-button       添加成功conect-title
    #
    # def test_cart_add(self):
    #     self.driver.find_element_by_id('q').send_keys('电视')
    #     self.driver.find_element_by_class_name('ecsc-search-button').click()
    #     self.driver.find_element_by_class_name('p-btn').click()
    #     #  切换frame
    #     self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
    #     # 验证 打印
    #     msg_cart = self.driver.find_element_by_xpath('//div[@class="conect-title"]/span').text
    #     assert msg_cart == "添加成功","断言提示信息，预期结果【添加成功】，实际结果【%s】"%msg_cart
    #     print('提示信息验证通过')






