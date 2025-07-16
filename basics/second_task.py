# Напиши функцию, которая принимает список строк и возвращает True, если все строки уникальны.
def list_cent(lst):
    set_cent = set(lst)
    if len(lst) == len(set_cent):
        return True
    return False

print(list_cent(['aboba', 'abobas', 'ccc']))
