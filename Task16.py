# Проверить, все ли числа в последовательности уникальны.

from ReadJson import read_json


data = read_json('task16.json')

print("The given list : ", data)

# Compare length for unique elements
if(len(set(data)) == len(data)):
    print("unique elements")
else:
   print("not unique elements")