# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

num = int(input())

first_digit = (num % 10**3) // (10**2)
second_digit = (num % 10**2) // (10**1)
third_digit = (num % 10**1) // (10**0)


print('Сумма цифр =', first_digit + second_digit + third_digit)
print('Произведение цифр =', first_digit * second_digit * third_digit)
