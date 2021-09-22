# Напишите программу, которая определяет наименьшее из четырёх чисел.

n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input()),

if n1 < n2:
    num1 = n1
else:
    num1 = n2
if n3 < n4:
    num2 = n3
else:
    num2 = n4

if num1 > num2:
    print(num2)
else:
    print(num1)