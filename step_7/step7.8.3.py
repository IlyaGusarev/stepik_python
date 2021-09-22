# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n в соответствии с примером:
# *
# **
# ***
# ****
# ***
# **
# *

import math
n = int(input())

half_n = math.ceil(n / 2)

for i in range(1, half_n + 1):
    for _ in range(i):
        print('*', end='')
    print()
for j in range(half_n -1, 0, -1):
    for _ in range(j):
        print('*', end='')
    print()

