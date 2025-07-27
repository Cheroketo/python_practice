kg = int(input('Ваш вес в килограммах '))
metr = float(input('Ваш рост в метрах '))
imt = kg/(metr*metr)

if imt < 18.5:
    print('Недостаточный вес')
elif imt>=18.5 and imt < 25:
    print('Нормальный вес')
else:
    print('Избыточный вес')