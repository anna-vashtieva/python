strings = sum(1 for line in open('text_5_2_txt', 'r', encoding='UTF-8'))
print('Количество строк в файле - ', strings)

i = 0
with open('text_5_2_txt', 'r', encoding='UTF-8') as f:
    while (i < strings):
        new_string = f.readline()
        print(len(new_string.split()))
        i += 1
