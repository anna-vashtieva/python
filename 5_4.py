rus = ['Один', 'Два', 'Три', 'Четыре']
i = 0
new_list = []

with open('text_5_4.txt', 'r') as f:
    for el in f:
        el = el.split(' ', 1)
        el[0] = rus[i]
        new_list.append(rus[i] + ' ' + el[1])
        i += 1
        print(" ".join(el))

with open('new_text_5_4.txt', 'w+', encoding='UTF-8') as new_f:
    new_f.writelines(new_list)
    print(new_f.read())
