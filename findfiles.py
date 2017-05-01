import os

find_key_word = input("请输入你想要寻找的文件或者包含关键字的文件:")
find_dir_place = input("请输入你所想要寻找的所在文件夹：")


def os_find_file(worksapace, key_file):
    ls = []     # 定义一个列表ls储存当输入的关键字被包含于文件名称时
    ls1 = []    # 定义一个列表ls储存当输入的关键字
    file_word = []
    ls3 = []
    ls4 = []
    for root, sub_file_name, files in os.walk(worksapace):
        for filepath in files:
            filepath = root + os.sep + filepath
            ls4 .append(filepath)
    for j in ls4:
        if key_file in j:
            recent_file = os.path.join(worksapace, j)
            ls.append(recent_file)
        if key_file not in j:
            other_file = os.path.join(worksapace, j)
            ls3.append(other_file)
            for i in ls3:
                with open(i, encoding='utf-8') as file:
                    key_word = file.read()
                    file_word.append(key_word)
                    if key_file in ''.join(file_word):
                        ls1.append(i)
    ls = list(set(ls + ls1))
    a = '\n'.join(ls)
    print(a)


os_find_file(find_dir_place, find_key_word)