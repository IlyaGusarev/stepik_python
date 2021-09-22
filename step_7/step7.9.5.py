# Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.

n = int(input())
total = 0
second_total = 1
for i in range(1, n + 1):
    second_total = 1
    for j in range(1, i + 1):
        second_total *= j
    total += second_total
print(total)