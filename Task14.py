# Посчитать, сколько раз символ встречается в строке.

# string = "Посчитать, сколько раз символ встречается в строке"
#
# symbol = "о"
#
# frequency = 0
# for digit in str(string):
#     if digit == symbol:
#         frequency += 1
# print(frequency)

from ReadJson import read_json


chars = "abcdefghijklmnopqrstuvwxyz"
check_string = read_json('task14.json')

res =[(char, check_string.count(char))
      for char in chars if check_string.count(char) > 1]

print(res)
