# Представьте, что у вас есть список слов. Вам нужно сгруппировать все слова, которые являются анаграммами друг друга.
# Анаграммы — это слова, состоящие из одних и тех же букв в разном порядке.



def group_angram(lst):
    group_dict = {}
    for element in lst:
        key = ''.join(sorted(element))
        if key in group_dict:
            group_dict[key].append(element)
        else:
            group_dict[key] = [element]

    return list(group_dict.values())


print(group_angram(["eat", "tea", "ate"]))


