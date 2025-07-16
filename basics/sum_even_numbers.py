# Напиши функцию sum_even_numbers(lst) — которая суммирует только чётные числа в списке.
def sum_even_numbers(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            count += lst[i]
    return count

print(sum_even_numbers([1,2,3,4,10]))