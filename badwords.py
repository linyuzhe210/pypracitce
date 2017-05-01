with open('屏蔽词.txt', 'r+', encoding='utf-8') as bad_words:
    def block_word(word):
        for j in word:
            if j.isupper() == 1:
                word = word.replace(j, j.lower())
        with open('屏蔽词.txt', 'r+', encoding='utf-8') as bad_words:
            for catch_word in bad_words:
                refresh = catch_word.strip()
                if refresh in word:
                    word = word.replace(refresh, '*'*len(refresh))
            print(word)
    while True:
        a = input("请输入你想要说的脏话(输入quit结束):")
        if a == 'quit':
            print('结束！')
            break
        block_word(a)
