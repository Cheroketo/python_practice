import random
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%"
len_passwd = int(input('Какой длины пароль ты хочешь? '))
passwd = ''
for i in range(len_passwd):
    passwd += random.choice(alphabet)
print(passwd)