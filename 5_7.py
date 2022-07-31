import json

firms = {}
prof = {}
sum_prof = 0

with open('text_5_7.txt', 'r') as f:
    for line in f:
        name, type_of_ownership, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms[name] = profit
        if profit > 0:
            sum_prof += profit
        else:
            profit = 0

prof['average_profit'] = sum_prof / sum(1 for line in open('text_5_7.txt', 'r'))
list = [firms, prof]

with open("list_5_7.json", "w") as write_f:
    json.dump(list, write_f)
