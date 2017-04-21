from random import *
loop_time = 1
round_time = 0
right_time = 0
lose_time = 0
sum_whole = 0
while True:
    round_time += 1
    num = randint(1, 101)
    loop_max = eval(input("请输入你想要猜几次:"))
    ans = eval(input("请输入你要猜的数字:"))
    while loop_time < loop_max:
        if ans < num:
            print("输小了")
            ans = eval(input("请输入你要猜的数字:"))
        if ans > num:
            print("输大了")
            ans = eval(input("请输入你要猜的数字:"))
        if ans == num:
            print("恭喜你猜对了")
            right_time += 1
            loop_time += 1
            break
        loop_time += 1
    while loop_time == loop_max:
        if ans < num:
            print("输小了")
        if ans > num:
            print("输大了")
        if ans == num:
            print("恭喜你猜对了")
            right_time += 1
            break
        print("你输入的次数已超过限制%d次,本次挑战失败." % loop_max)
        lose_time += 1
        break
    sum_whole += loop_time
    loop_time = 1  # 计数器重置
    print("你准备继续挑战吗?输入(Y)继续猜，输入(N)结束:")
    togo = input()
    if togo == 'Y':
        continue
    elif togo == 'N':
        pass
    print("你已经玩了%d回合，做对了%d次,失败了%d次，总共猜了%d次，平均每回合猜%.1f次，游戏结束" % (round_time, right_time, lose_time, sum_whole, sum_whole / float(round_time)))
    break
