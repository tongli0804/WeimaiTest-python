
from random import randint
###构造程序逻辑

'''水仙花
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$
'''

def shuixianhua():
    for num in range (100,1000):
        gewei = num % 10
        shiwei = num // 10 % 10
        baiwei = num //100
        if num == gewei ** 3 + shiwei ** 3 + baiwei ** 3:
            print(num)


'''
正整数的反转
'''
def shuzifanzhuan():
    num = int(input("请输入数字"))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)


'''
百钱百鸡问题
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
'''
def baiqian():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，
如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。

我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
'''
def CRAPS():
    money = 1000
    global nextnumcount, wanjiacount, zhuangjiacount
    nextnumcount = 0
    wanjiacount = 0
    zhuangjiacount = 0
    while money > 0:
        need_go_on = False
        firstnum = randint(2,12)
        print('玩家摇出了%d点' % firstnum)
        if firstnum == (7 | 11):
            money = money + 100
            print("玩家胜，资金还有%d元" % money)
            wanjiacount += 1
        elif firstnum == (2 | 3|12):
            money = money - 100
            print("庄家胜，资金还有%d元" % money)
            zhuangjiacount += 1
        else:
            print("继续摇色子")
            need_go_on = True
            nextnumcount += 1
        while need_go_on:
            need_go_on = False
            nextnum = randint(2,12)
            print('玩家继续摇出了%d点' % nextnum)
            if nextnum == 7:
                money = money - 100
                print("庄家胜，资金还有%d元" % money)
                zhuangjiacount += 1
            elif nextnum ==  firstnum:
                money = money + 100
                print("玩家胜，资金还有%d元" % money)
                wanjiacount += 1
            else:
                print("继续摇色子")
                need_go_on = True
                nextnumcount += 1
        count = nextnumcount + wanjiacount + zhuangjiacount
        print("总共摇了%d次,庄家胜%d次，玩家胜%d次" % (count,zhuangjiacount,wanjiacount))


'''
生成斐波那契数列的前20个数
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''


'''
找出10000以内的完美数
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
'''


'''
输出100以内所有的素数
素数指的是只能被1和自身整除的正整数（不包括1）
'''








if __name__ == '__main__':
    # shuixianhua()
    # shuzifanzhuan()
    # baiqian()
    CRAPS()



