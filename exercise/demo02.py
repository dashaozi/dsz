# -*- coding: utf-8 -*-
__author__ = 'shaoyn'
__date__ = '2020/8/2 21:10'


"""
用类和面向对象的思想，
“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），
数量为5个
"""


# 定义类，以橘子为例
class Tangerine:
    """
    属性
    颜色=橘色 or 绿色
    种类=水果
    形状=球体
    方法
    绿色的=吃起来酸
    橘色的=吃起来甜
    """
    # 定义属性
    name = "橘子"
    color ="orange"
    kind = "fruits"
    shape = "sphere"
    # 定义类

    def sour(self):
        print("吃起来酸")

    def sweet(self):
        print("吃起来甜")


# 输出属性
print(Tangerine.name,"颜色是",Tangerine.color)
#类的实例化
tangerine = Tangerine()
# 调用函数
tangerine.sweet()
