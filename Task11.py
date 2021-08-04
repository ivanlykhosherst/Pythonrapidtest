# Принимать на вход два списка и выводить все элементы первого, которых
# нет во втором.

from ReadJson import read_json


data = read_json('task11.json')
print(set(data[0]) - set(data[1]))
