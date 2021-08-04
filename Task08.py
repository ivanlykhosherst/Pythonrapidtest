# Вывод первого и последнего элемента массива

from ReadJson import read_json


cars = read_json('task08.json')
print(f'First element is:{cars[0]}\nLast element is:{cars[-1]}')

