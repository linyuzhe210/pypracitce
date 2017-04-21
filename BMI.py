a = eval(input("请输入你的身高(kg):"))
b = eval(input("请输入你的体重(m):"))

BMI = b / a ** 2
if BMI < 18.5:
    print("%.1f,体重偏轻" % BMI)
elif 24 > BMI >= 18.5:
    print("%.1f,体重正常" % BMI)
elif BMI >= 24:
    print("%.1f,体重偏重" % BMI)