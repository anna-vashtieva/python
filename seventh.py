distance_start = float(input('Введите расстояние (км), которое пробежал спортсмен в первый день - '))
distance_finish = float(input('Введите величину дистанции (км), которую спортсмен должен достичь - '))
i = 0

while distance_start < distance_finish:
    distance_start = distance_start + distance_start * 0.1
    i = i + 1
    print(i, '-й день - ', distance_start, 'км')

print('На ', i, '-й день спортсмен достиг результата - не менее ', distance_finish, 'км')
