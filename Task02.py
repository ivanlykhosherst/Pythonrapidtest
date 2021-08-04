# Для слияния нескольких (от 2 до N) словарей в один.

from MergeDicts import merge_dicts
from ReadJson import read_json


data2 = read_json('task02.json')
print(merge_dicts(data2[0], data2[1], data2[2]))
