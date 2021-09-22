# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

num = int(input())
same_dig = False
if num < 11:
    print('NO')
else:
    while same_dig == False and num > 9:
        n = num % 10
        m = (num // 10) %10
        if n <= m and m != 0:
            same_dig = False
        else:
            same_dig = True

        num = num // 10
    if same_dig == True:
        print('NO')
    else:
        print('YES')


