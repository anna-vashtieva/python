# запрос данных у пользователя
revenue = int(input('Введите значение выручки фирмы - '))
costs = int(input('Введите значение издержек фирмы - '))

# условный оператор для определения в прибыль или убыток работает фирма
if revenue > costs:
    print('Поздравляем! Фирма работает в прибыль')
else:
    print('К сожалению фирма работает в убыток. Нужно что-то менять')
