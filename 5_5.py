result = 0

with open('text_5_5.txt', 'w') as f:
    f.write('10 20 30 40 50')

numbers = open('text_5_5.txt', 'r').read().split()
for el in numbers:
    result += float(el)

print(result)
