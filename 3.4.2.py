x = int(input('Введите целое положительное число - '))
y = int(input('Введите целое отрицательное число - '))

def my_func(x, y):
    i = 1
    koef = 1
    if y >= 0:
        print('Следует ввести отрицательное число, пожалуйста, повторите ввод: ')
        y = int(input('Введите целое отрицательное число - '))
    while i <= abs(y):
        degree = koef*x
        koef = degree
        i += 1
    return 1/degree

print(my_func(x, y))
