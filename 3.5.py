result = 0

while True:
    data = input('Введите числа через пробел: ').split()
#    sum_list = list(map(int, data))
    for el in data:
        try:
            number = float(el)
            result += number
        except:
            if el == '!':
                print('Был введен символ "!", суммирование прекращено')
                print('Сумма всех введенных чисел: ', result)
                exit()
            else:
                print('Был введен недопустимый символ')
                print('Сумма всех введенных чисел: ', result)
                exit()
