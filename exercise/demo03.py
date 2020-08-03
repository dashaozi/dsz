# -*- coding: utf-8 -*-
__author__ = 'shaoyn'
__date__ = '2020/8/2 21:09'
# 1111

"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造

"""


# 定义一个天山童姥类 ，类名为TongLao
class Tonglao:
    # 属性有血量，武力值（通过传入的参数得到）
    # 定义构造函数
    def __init__(self,tong_hp,tong_power):
        # 定义属性天山童姥的武力值和血量
        self.tong_hp = tong_hp
        self.tong_power = tong_power
    # see_people方法，需要传入一个name参数
    # 定义函数
    def see_people(self,name):
        # 如果传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if name == "WYZ":
            print("师弟！！！！")
        # 如果传入“李秋水”，打印“呸，贱人”
        elif name == "李秋水":
            print("呸，贱人")
        # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    # 定义fight_zms方法（天山折梅手）
    def fight_zms(self,enemy_hp,enemy_power):
        # 调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        # 定义属性，敌人的血量和武力值
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power

        # 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
        # 天山童姥使用天山折梅手（使用之后武力值*10，血量/2）增加自身能力，与敌人PK
        self.tong_hp = self.tong_hp/2 - self.enemy_power
        self.enemy_hp = self.enemy_hp - self.tong_power*10

        if self.tong_hp <= 0:
            print("天山童姥的剩余血量为",self.tong_hp)
            print("敌人的剩余血量为", self.enemy_hp)
            print("天山童姥输了")
        elif self.enemy_hp <= 0:
            print("天山童姥的剩余血量为",self.tong_hp)
            print("敌人的剩余血量为", self.enemy_hp)
            print("敌人输了")
        else:
            # 给出警告
            raise Exception("不允许平局")
# 类的实例化，并赋值
tonglao = Tonglao(1000,200)
# 调用函数并赋值
tonglao.see_people("李秋水")
tonglao.fight_zms(1000,200)
