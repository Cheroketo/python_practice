def intersection(lst1, lst2):
    lst3 = list()
    for element in lst1:
            if element in lst2:
                lst3.append(element)
    return list(set(lst3))


print(intersection([1,2,3], [2,3,4]))