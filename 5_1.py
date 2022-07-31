with open('new.txt', 'w') as f:
    while True:
        phrase = input('Введите данные: ')
        if not phrase:
            print('Вы прервали ввод данных')
            break
        else:
            with open('new.txt', 'a', encoding='UTF-8') as f:
                f.write(phrase + '\n')
