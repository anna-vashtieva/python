number_of_month = int(input('Введите номер месяца от 1 до 12 - '))

year_list = ['зима', 'весна', 'лето', 'осень']
if number_of_month == 12 or number_of_month < 3:
    print(year_list[0])

elif 3 <= number_of_month < 6:
    print(year_list[1])

elif 6 <= number_of_month < 9:
    print(year_list[2])

else: print(year_list[3])
