rating = [7, 5, 3, 3, 2]

new_el = int(input('Введите натуральное число - '))

if new_el <= 0:
    print('Следует ввести натуральное число (целое число больше нуля)')

else:
    i = 0
    if new_el > rating[0]:
        rating.insert(0, new_el)
    elif new_el in rating:
        rating.insert(rating.index(new_el), new_el)
    elif new_el < rating[len(rating) - 1]:
        rating.append(new_el)
    else:
        while i < len(rating) - 1:
            if new_el > rating[i]:
                rating.insert(i, new_el)
                break
            else:
                i += 1
    print(rating)
