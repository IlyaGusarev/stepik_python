# На вход программе подаётся три целых числа: a1, d, n каждое на отдельной строке.
# Программа должна вывести nn-ый член арифметической прогрессии.

a1 = int(input())
d = int(input())
n = int(input())

print(a1 + d * (n - 1))