def quotient():
    arg1 = float(input('Введите делимое - '))
    arg2 = float(input('Введите делитель - '))
    if arg2 == 0:
        print('Целочисленное деление на ноль является критической ошибкой, попробуйте ввести другое число:')
        arg2 = float(input('Введите делитель, не равный нулю -'))
    return arg1 / arg2

print(quotient())
