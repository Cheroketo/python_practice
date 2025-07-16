def palindrome_new(str):
    clean_str = ''.join(i.lower() for i in str if i.isalnum())
    return clean_str == clean_str[::-1]
print(palindrome_new('казак'))