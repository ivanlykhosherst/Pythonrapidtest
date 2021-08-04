# В принимаемом тексте выводит два слова: наиболее часто встречающееся
# и самое длинное.

from MostFreqWord import most_frequent
from ReadJson import read_json


data = read_json('task17.json')

# Finding longest word
longest = max(data.split(), key=len)
frequent = most_frequent(data)

# Displaying longest word & most frequent word
print(f"Longest word is:{longest}\nMost frequent word is:{frequent}")
