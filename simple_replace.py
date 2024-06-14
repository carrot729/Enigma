from alive_progress import alive_bar


def simple_replace(password, replace_word1, replace_word2, replace_word3):
    count = 0  # 设置计数器
    new_pass = ''  # 设置一个空字符串准备接收密码
    ori_table = 'abcdefghijklmnopqrstuvwxyz'  # 原始的字符串，用来建立映射表
    with alive_bar(len(password)) as bar:
        for obj in password:  # 开始拆解原字符串
            bar()
            if obj == ' ':
                new_pass += obj
                continue
            table1 = str.maketrans(ori_table, replace_word1)  # 建立转子1的映射表
            table2 = str.maketrans(ori_table, replace_word2)  # 建立转子2的映射表
            table3 = str.maketrans(ori_table, replace_word3)  # 建立转子3的映射表
            new_obj = str.translate(obj, table1)  # 把obj通过转子1转换
            new_obj = str.translate(new_obj, table2)  # obj通过转子2
            new_obj = str.translate(new_obj, table3)  # obj通过转子3
            new_obj = reverse_word(new_obj)  # 进入自反器，得到自反值
            reverse_table1 = str.maketrans(replace_word1, ori_table)  # 增加自反出去的对应表，反向解译
            reverse_table2 = str.maketrans(replace_word2, ori_table)
            reverse_table3 = str.maketrans(replace_word3, ori_table)
            new_obj = str.translate(new_obj, reverse_table3)  # new_obj再赋值，反向解译通过转子3
            new_obj = str.translate(new_obj, reverse_table2)  # 通过转子2
            new_obj = str.translate(new_obj, reverse_table1)  # 通过转子1
            new_pass += new_obj  # 返回的密码增加一个new_obj
            replace_word1 = rotors(replace_word1)  # 转子1每个字符都转动一次
            count += 1  # 计数器增加1
            if count % 676 == 0:  # 如果模676为0，那么转子3转动一次(因为转子2已经转动了一整圈）
                replace_word3 = rotors(replace_word3)
            elif count % 26 == 0:  # 如果模26为0，那么转子2转动一次（因为转子1已经转动了一整圈）
                replace_word2 = rotors(replace_word2)

    return new_pass  # 返回新的已经被转子加密的密码


def reverse_word(word):
    dic = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q',
           'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y',
           'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
           'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm'}
    return dic[word]


def rotors(replace_word):  # 转子转动的函数，每调用一次，就把转子前面第一个字母移动到最后
    return replace_word[1:] + replace_word[0]
