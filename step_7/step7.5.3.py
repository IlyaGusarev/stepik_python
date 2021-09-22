# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
total = 0
counter = 0
product = 1
average = 0
first_digit = 0
first_plus_last = 0

n = len(str(num))
first_plus_last = (num%(10**n)//10**(n-1)) + num%10

while num != 0:
    first_digit = num
    last_digit = num % 10
    total += last_digit
    counter += 1
    product *= last_digit
    average = total / counter
    num = num // 10
print(total, counter, product, average, first_digit, first_plus_last, sep='\n')

