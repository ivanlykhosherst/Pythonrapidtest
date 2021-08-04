# Вывести чётные числа из заданного списка и останавливается, если
# встречаешь число 237.

from ReadJson import read_json


data = read_json('task10.json')

for num in data:

    # check if even and break when it's 237
    if num == 237:
        break
    elif num % 2 == 0:
        print(num, end=" ")
    else:
        pass
