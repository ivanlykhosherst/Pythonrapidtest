import json
import random

data = {}

for i in range(1, 11):
    data['key'+str(i)] = random.randrange(1, 50)

with open('task01.json', 'w') as outfile:
    json.dump(data, outfile)
