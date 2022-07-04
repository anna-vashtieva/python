# запрос данных у пользователя
revenue = int(input('Введите значение выручки фирмы - '))
costs = int(input('Введите значение издержек фирмы - '))

# условный оператор для определения
if revenue > costs:
    print('Поздравляем! Фирма работает в прибыль')

    profitability = (revenue - costs)/revenue
    print('Рентабельность фирмы составляет - ', profitability)

    staff = int(input('Введите численность сотрудников фирмы - '))

    profit_one = (revenue - costs)/staff
    print('Прибыль фирмы в расчете на одного сотрудника - ', profit_one)

else:
    print('К сожалению фирма работает в убыток. Нужно что-то менять')
