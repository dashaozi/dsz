# -*- coding: utf-8 -*-
__author__ = 'shaoyn'
__date__ = '2020/8/9 11:24'
"""
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""
import pytest
import yaml
from pythoncode.calc import Calculator
# 打开yml文件，并调取数据
with open("./dates/calc.yml", encoding='utf-8') as f:
    dates = yaml.safe_load(f)
    add_dates = dates['add']['dates']
    # print(adddates)
    my_id = dates['add']['myid']
    # print(myid)
    # dates = yaml.safe_load(f)
    div_dates = dates['div']['dates']
    print(div_dates)
    my_id1 = dates['div']['myid']
    print(my_id1)

class TestCalc():
    # 定义类级结构，在类的前后各执行一次
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardowm_class(self):
        print("结束计算")
    # 定义方法级结构，在用例的前后各执行一次
    def setup_method(self):
        print("测试用例开始")

    def teardown_method(self):
        print("测试用例结束")
    # @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', add_dates, ids=my_id)
    # @pytest.mark.add
    def test_add(self, a, b, expect):
        # 实例化计算器
        # calc = Calculator()
        # 调用相加add()方法
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(a,str):
            assert expect != result
        elif isinstance(b,str):
            assert expect != result
        # 断言
        assert expect == result

    # @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', div_dates, ids=my_id1)
    def test_div(self,a,b,expect):
        result = self.calc.div(a, b)
        if b == 0:
            assert expect != result
            # 断言
        assert expect == result


