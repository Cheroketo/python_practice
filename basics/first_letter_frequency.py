def first_letter_frequency(words_lst):
    dict_result = {}
    for word in words_lst:
        first_letter = word[:1]
        if first_letter in dict_result:
            dict_result[first_letter] += 1
        else:
            dict_result[first_letter] = 1
    return dict_result

print(first_letter_frequency(["apple", "apricot", "banana"]))