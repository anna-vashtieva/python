from functools import reduce

data = [el for el in range(10, 1001, 2)]
print(reduce((lambda x, y: x * y), data))
