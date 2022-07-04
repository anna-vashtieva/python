data_list = input("Введите элементы списка через пробел без знаков препинания: ").split()
print('Введенный Вами список: ', data_list)

for i in range(0, len(data_list) - 1, 2):
    data_list[i], data_list[i+1] = data_list[i+1], data_list[i]

print('Преобразованный список: ', data_list)
