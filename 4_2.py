data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_data = [data[i] for i in range(1, len(data)) if data[i-1] < data[i]]
print(new_data)
