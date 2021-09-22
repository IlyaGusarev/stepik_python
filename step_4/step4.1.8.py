# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

num1, num2, num3 = int(input()), int(input()), int(input())
count = 0

if num1 > 0:
    count = count + num1
if num2 > 0:
    count = count + num2
if num3 > 0:
    count = count + num3
print(count)