message = "Это очень плохой пример"
bad_words = ["плохой", "ужасный"]
for i in bad_words:
    if i in message:
        print('Сообщение не прошло цензуру.')
        break
else:
    print('Все в порядке')

