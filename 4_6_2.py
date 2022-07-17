from itertools import cycle

i = 0
for el in cycle(['A', 'B', 'C']):
    print(el)
    if i > 9:
        break
    i += 1
