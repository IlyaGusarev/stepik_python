# На вход программе подаётся три целых числа: b1, q, n, каждое на отдельной строке.
# Программа должна вывести n-ый член геометрической прогрессии.

b1 = int(input())
q = int(input())
n = int(input())

bn = b1 * q**(n - 1)

print(bn)
