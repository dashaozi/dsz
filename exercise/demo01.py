# -*- coding: utf-8 -*-
__author__ = 'shaoyn'
__date__ = '2020/8/2 21:11'

"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""


def fight():
    # 定义四个变量，存放对打双方的血量值（hp)和攻击力值（power)
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 200
# 对打多轮，谁的hp先为0，那么谁就输了
    # 使用while循环进行多轮PK
    while True:
        # 甲方血量值=自身血量值-乙方攻击力值
        my_hp = my_hp - your_power
        # 乙方血量值=自身血量值-甲方攻击力值
        your_hp = your_hp - my_power
        # 如果甲方血量值<=0，甲方输出"我赢了"
        if my_hp <= 0:
            print("我赢了")
            break
        # 如果甲乙方血量值<=0，甲方输出"我赢了"
        elif your_hp <= 0:
            print("我输了")
            break


# 调用fight函数
fight()



