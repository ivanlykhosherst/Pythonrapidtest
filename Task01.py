# Сортировка словаря с целыми числами по в порядке возрастания и
# убывания.

from ReadJson import read_json

data2 = read_json('task01.json')
print(data2)

print(sorted(data2.values()))
print(sorted(data2.values(), reverse=True))
