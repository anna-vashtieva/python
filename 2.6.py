products = input("Введите названия товаров через пробел без знаков препинания: ").split()

i = 0
num = 1

data_products = []

while i < len(products):
    print('Введите данные для товара', products[i], ': ')
    price = float(input('Введите цену товара - '))
    amount = int(input('Введите количество товара - '))
    unit = str(input('Введите единицы измерения товара - '))

    products_dict = {
        'название': products[i],
        'цена': price,
        'количество': amount,
        'ед.': unit
    }
    data_tuple = (num, products_dict)
    data_products.append(data_tuple)
    i += 1
    num += 1

print('Структура данных "Товары": ')
print(data_products)

analytics_dict = {}

for product in data_products:
    for key, value in product[1].items():
        if key in analytics_dict:
            analytics_dict[key].append(value)
        else:
            analytics_dict[key] = [value]

print('Аналитика о товарах: ')
print(analytics_dict)
