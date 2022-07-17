data_list = input("Введите несколько слов через пробел без знаков препинания: ").split()

for ind, el in enumerate(data_list, 1):
    print(ind, el[0:10])
