# -*- coding: utf-8 -*-
__author__ = 'shaoyn'
__date__ = '2020/8/10 19:55'
"""
1、补全计算器（加减乘除）的测试用例
2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别
"""
import pytest
import yaml
from pythoncode.calc import Calculator
# 打开yml文件，并调取数据
class TestCalc():
    # @pytest.mark.parametrize('a,b,expect', add_dates, ids=my_id)
    # @pytest.mark.add
    def test_add(self, get_calc, get_dates):
        result = get_calc.add(get_dates[0], get_dates[1])
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(get_dates[0],str):
            assert get_dates[2] != result
        elif isinstance(get_dates[1],str):
            assert get_dates[2]!= result
        # 断言
        assert get_dates[2] == result

    # @pytest.mark.div
    # @pytest.mark.parametrize('a,b,expect', div_dates, ids=my_id1)
    def test_div(self,get_calc,get_dates1):
        result = get_calc.div(get_dates1[0], get_dates1[1])
        if get_dates1[1] == 0:
            assert get_dates1[2] != result
            # 断言
        assert get_dates1[2] == result

    def check_sub(self,get_calc,get_dates2):
        result = get_calc.sub(get_dates2[0], get_dates2[1])
        if isinstance(result, float):
            result = round(result, 2)
        elif isinstance(get_dates2[0],str):
            assert get_dates2[2] != result
        elif isinstance(get_dates2[1],str):
            assert get_dates2[2]!= result
        assert get_dates2[2] == result

    def check_mul(self, get_calc, get_dates3):
        result = get_calc.mul(get_dates3[0], get_dates3[1])
        assert get_dates3[2] == result






