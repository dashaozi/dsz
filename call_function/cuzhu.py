# -*- coding: utf-8 -*-
__author__ = 'shaoyn'
__date__ = '2020/8/2 21:03'
from exercise.demo03 import Tonglao;
"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
# 111
# 定义类，并且继承Tonglao类
class Xuzhu(Tonglao):
    # 定义构造函数，并继承父类的构造函数
    def __int__(self):
        # 继承并赋值
        super().__init__(1000,200)
        pass
    # 定义函数
    def read(self):
        # 输出
        print("罪过罪过")
# 实例化
xuzhu = Xuzhu(1000,200)
# 调用函数
xuzhu = xuzhu.read()
