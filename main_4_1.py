import sys
from calc_4_1 import calc_wage

print(sys.argv)

try:
    print(calc_wage())
except Exception as e:
    if 'DEBUG' in sys.argv:
        print(e)
    else:
        print('Ошибка')

