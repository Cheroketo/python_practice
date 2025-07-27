numbers = [12, 75, 150, 180, 145, 525, 50]
for element in numbers:
    if element % 5 == 0:
        if 150 < element < 500:
            continue
        elif element > 500:
            break
        else:
            print(element)
