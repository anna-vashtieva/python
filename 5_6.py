import re
s = {}

with open('text_5_6.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        subj, hours = line.split(":", 1)
        hours = [float(hours) for hours in re.findall(r'-?\d+\.?\d*', hours)]
        s[subj] = sum(hours)
print(s)
