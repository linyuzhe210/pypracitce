import random


def three_doors(boolean):
    lst = ['car', 'sheep', 'sheep']
    random.shuffle(lst)
    num = random.randint(0, 2)
    choice = lst.pop(num)
    if choice == 'car' and boolean:
        ext = random.choice(lst)
        lst.remove(ext)
        return lst[0]
    elif choice == 'sheep' and boolean:
        lst.pop(lst.index('sheep'))
        return lst[0]
    return choice

true_time = 0
false_time = 0
sum_ = 0
_sum = 0
for i in range(2, 10003):
    if i % random.randint(2, 4) == 0:
        result = three_doors(True)
        if result == 'car':
            sum_ += 1
        true_time += 1
    else:
        result = three_doors(False)
        if result == 'car':
            _sum += 1
        false_time += 1

print('switch: %d \nswitch win: %.2f %%' % (true_time, sum_ / true_time * 100))
print('stay: %d\nstay win: %.2f %%' % (false_time, _sum / false_time * 100))

