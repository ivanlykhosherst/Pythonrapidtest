# Нахождение трёх ключей с самыми высокими значениями в словаре
from ReadJson import read_json


data = read_json('task03.json')
sort_d = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print(list(sort_d.keys())[:3])
