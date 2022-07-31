total_income = 0
with open('text_5_3.txt', 'r', encoding='UTF-8') as f:
    print('Сотрудники, имеющие оклад менее 20 тысяч: ')
    for el in f:
        key, value = el.split()
        if float(value) < 20000.00:
            print(el)
        total_income += float(value)

average_income = total_income / sum(1 for line in open('text_5_3.txt', 'r', encoding='UTF-8'))
print('Средний доход - ', round(average_income, 2))
