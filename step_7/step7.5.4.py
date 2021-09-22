# Дано натуральное число n (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

num = int(input())
last_digit = 0
sec_digit = 0
while num != 0:
    last_digit, sec_digit = num % 10, last_digit
    num = num // 10
print(sec_digit)


