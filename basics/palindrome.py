def palindrome(str):
    if str == str[::-1]:
        return f'Является палиндромом'
    else:
        return f'Не является'