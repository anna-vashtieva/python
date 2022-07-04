number_of_month = int(input('Введите номер месяца от 1 до 12 - '))

if number_of_month < 1 or number_of_month > 12:
    print('Введены некорректные данные')

year_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for key in year_dict.keys():
    if number_of_month in year_dict[key]:
        print(key)
