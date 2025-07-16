def number_frequency(lst):
    dict_result = {}
    for num in lst:
        if num in dict_result:
            dict_result[num] += 1
        else:
            dict_result[num] = 1
    return dict_result
print(number_frequency([1,1,2,3,3,3,4]))