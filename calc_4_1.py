output = input('Введите выработку сотрудника в часах - ')
rate = input('Введите размер ставки за один час работы - ')
bonus = input('Введите размер премии - ')

def calc_wage():
    return float(output) * float(rate) + float(bonus)
