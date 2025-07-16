def min_word_lst(lst_strings):
    index = 0
    max_leng = float('inf')
    for i in range(len(lst_strings)):
        if len(lst_strings[i]) < max_leng:
            max_leng = len(lst_strings[i])
            index = i
    return lst_strings[index]
print(min_word_lst(['abc', 'a', 'ssdrerfc']))
