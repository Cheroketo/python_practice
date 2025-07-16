def uniq_list(lst):
    lst_new = list()
    for i in range(len(lst)):
        if lst[i] not in lst_new:
            lst_new.append(lst[i])
    return lst_new
print(uniq_list([1,3,4,3,2]))