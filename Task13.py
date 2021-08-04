# Сложить цифры целого числа заданного пользователем

print('Enter integer value:')
number = input()

sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)

print(sum_of_digits)
