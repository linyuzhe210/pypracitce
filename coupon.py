import string
import random

code = string.digits + string.ascii_letters
time = eval(input("请输入你想要生成奖券号码的次数:"))
ls = list(set([''.join(random.sample(code, 8)) for x in range(time)]))
for i in ls:
    print(i)
