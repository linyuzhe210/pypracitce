def my_func(length, height, sign):
    for i in range(height):
        for j in range(length):
            print("%c" % sign, end='')
        print("\n", end='')
my_func(5, 5, '*')
my_func(3, 4, '*')
my_func(5, 2, '!')