def max_proizvedenie(lst):
    max1 = max2=float('-inf')
    for num in lst:
        if num>max1:
            max2 = max1
            max1 = num
        elif num>max2:
            max2 = num
    return max1*max2