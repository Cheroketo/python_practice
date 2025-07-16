def chanks(lst, n):
    lst_result = []
    for i in range(0, len(lst), n):
        lst_result.append(lst[i:i+n])
    return ", ".join(str(chunk) for chunk in lst_result)

print(chanks([1,2,3,4], 2))