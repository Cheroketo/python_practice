def avg_word_length(text):
    lst_strings = text.split()
    lst_count_string = list()
    for i in lst_strings:
        lst_count_string.append(len(i))
    return sum(lst_count_string)/len(lst_count_string)
print(avg_word_length('привет мир'))