def string_dict_counter(str):
    dict_result = {}
    lst_str = list(str.lower())
    for element in lst_str:
        if element.isalpha() and element in dict_result:
            dict_result[element] += 1
        elif element.isalpha():
            dict_result[element] = 1
    return dict_result


print(string_dict_counter('ABHDSDV11:'))
