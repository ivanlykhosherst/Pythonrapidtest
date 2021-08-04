# С помощью анонимной функции извлечь из списка числа, делимые на 15.

from ReadJson import read_json


data = read_json('task15.json')
new_list = list(filter(lambda x: (x % 15 == 0), data))

print(new_list)
