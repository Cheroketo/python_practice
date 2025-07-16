def split_list(lst, n):
    lst_new = []
    for i in range(0, len(lst), n):
        lst_new.append(lst[i:i+n])
    return lst_new


print(split_list([1,2,3,4,5], 0))
