# '''
# 计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
# 计算机给出对应的提示信息（大一点、小一点或猜对了），
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，
# 否则游戏继续。
# '''
# import random
#
# shuzi = random.randint(1, 100)
# count = 0
#
# while True:
#     count = count + 1
#     num = input()
#
#     if num > shuzi:
#         print("数字大了点，再来一次")
#
#     elif num < shuzi:
#         print("数字小了点，再来一次")
#
#     else:
#         print("你猜中了，花了%d次" % count)
#         break
#
from datetime import date
from time import time

print("hello")
