import json


mylist1 = "Stockholm is the capital of Sweden It has the most populous urban area in Sweden as well as in Scandinavia"


with open('task17.json', 'w') as outfile:
    json.dump(mylist1, outfile)
