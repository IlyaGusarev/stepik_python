# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

num1 = int(input())

print('Следующее за числом', num1, 'число:', num1 + 1)
print('Для числа', num1, 'предыдущее число:', num1 - 1)