# написать функцию которая принимает массив и чило таргет. Надо написать индексы которые в сумме дают таргет

def twoSum(nums, target):
    lst_indexex = list()
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] + nums[j] == target:
                lst_indexex.append(j)
                lst_indexex.append(i)
    return lst_indexex

print(twoSum([3,2,4], 6))