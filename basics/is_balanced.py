def is_balanced(lst):
    mid = len(lst) // 2
    if sum(lst[:mid]) == sum(lst[-mid:]):
        return True
    else:
        return False

print(is_balanced([1, 2, 3, 3, 2, 1]))