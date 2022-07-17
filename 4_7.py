n = int(input('Введите целое число - '))

i = 1
def fact(n):
    data = [el for el in range(1, n + 1)]
    for el in data:
        yield el
        print('Следующее значение')

factorial = fact(n)

for el in factorial:
    result = i * el
    i = result
    print(result)
