import allure
import pytest

# class Test:
#     def test_case01(self):
#         print(1)
#
#     def test_case02(self):
#         print(2)
#
#
# # 通过 入口函数 main执行
#
# if __name__ == '__main__':
#     pytest.main(['-s','test_demo.py'])
#
#
#
#
# # 函数级别方法
#
# class Test_01:
#
#     def setup(self):
#         print('test------->setup')
#     def teardown(self):
#         print('test------->teardown')
#     def test_case01(self):
#         print('test----->1')
#     def test_case02(self):
#         print('test------>2')
#
# # 类方法
# class Test_02:
#     def setup_class(cls):
#         print('test--->setupclass')
#     def teardown_class(cls):
#         print('test---->teardownclass')
#     def test_case01(self):
#         print('test----->1')
#     def test_case02(self):
#         print('test------>2')
#
#
# # 控制函数执行顺序   需要优先执行test—case03
#
#
# class Test_order:
#
#     def test_case01(self):
#         print('test----->1')
#     @pytest.mark.run(order=2)
#     def test_case02(self):
#         print('test------>2')
#     @pytest.mark.run(order=1)
#     def test_case03(self):
#         print('test----->3')
#
#
# # 失败重试
#
# class Test_reruns:
#     def test_a(self):
#         assert 1==1
#
#
#     def test_b(self):
#         print('失败')
#         assert 1==2
#
#
# # 跳过函数
#
# class Test_skip:
#     def test_a(self):
#         assert 1==1
#
#     @pytest.mark.skip(reason='当前版本不支持')
#     def test_b(self):
#         print('失败')
#         assert 1==2
#
# # 预期失败
#
# class Test_xfail:
#     def test_a(self):
#         print('----testa---')
#         assert 1==1
#
#     @pytest.mark.xfail()
#     def test_b(self):
#         print('----testb---')
#         assert 0==1
#
#     @pytest.mark.xfail()
#     def test_c(self):
#         print('----testc---')
#         assert 0==2
#
# # 数据参数  单个参数
#
# class Test_para:
#     @pytest.mark.parametrize('age',[18,5,7,8])
#     def test_a(self,age):
#         print(age)
#
# # 数据参数化  多个参数
#
#
# class Test_paras:
#     @pytest.mark.parametrize(('name','age'),[('zhangsan',18),('lisi',19)])
#     def test_a(self,name,age):
#         print(name,age)




# 登录   用户a需要先登录   用户b不需要登录   用例c需要登录
# fixture使用
#
# class Test_fixture:
#
#     @pytest.fixture()
#     def login(self):
#         print('登录操作')
#         uname = 'lily'
#         return uname
#
#     def test_a(self,login):
#         print(f'test_a{login}')
#
#     def test_b(self):
#         print('不需要登录')
#
#     def test_c(self,login):
#         print(f'test_c{login})')




class Test_allure:

    @pytest.fixture()
    def login(self):
        print('登录操作')
        uname = 'lily'
        return uname
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title='需要登录')
    def test_a(self,login):
        print(f'test_a{login}')

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.feature('testb模块')
    def test_b(self):
        print('不需要登录')

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title='testc需要登录')
    @allure.feature('testc模块')
    def test_c(self,login):
        print(f'test_c{login})')








