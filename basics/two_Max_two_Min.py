def two_Max_two_Min(lst):
    max1=max2=float('-inf')
    min1=min2=float('inf')
    for element in lst:
        if element >max1:
            max2 = max1
            max1 = element
        elif element > max2:
            max2 = element
    for element in lst:
        if element <min1:
            min2 = min1
            min1 = element
        elif element < min2:
            min2 = element
    return max1*max2 > min1+min2
print(two_Max_two_Min([1,2,3,4,5]))