# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии

n1, n2, n3 = int(input()), int(input()), int(input())


if n2 - n1 == n3 - n2:
    print('YES')
else:
    print('NO')