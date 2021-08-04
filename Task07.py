# Преобразования полученных от пользователя последовательность чисел,
# разделенных запятой в список и кортеж с этими числами

L = [int(x) for x in input("Enter multiple values\n").split(',')]
print("\nList", L)
print("\nTuple", tuple(L))