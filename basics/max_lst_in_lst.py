def max_list_in_list(lst):
    lst_max = []
    for element in lst:
        max = float('-inf')
        for j in element:
            if j > max:
                max = j
        lst_max.append(max)
    return lst_max
print(max_list_in_list([[1,2,3],[2,3,6,8]]))