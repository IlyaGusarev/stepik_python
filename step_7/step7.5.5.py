# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

num = int(input())
same_dig = False
if num < 10:
    print('YES')
else:
    while same_dig == False and num != 0:
        n = num % 10
        m = (num // 10) %10
        if n != m and m > 0:
            same_dig = True
        num = num // 10
    if same_dig == True:
        print('NO')
    else:
        print('YES')


