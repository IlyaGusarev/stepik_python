# Дан порядковый номер месяца (1...12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.

num = int(input())
if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
    print(31)
elif num == 4 or num == 6 or num == 9 or num == 11:
    print(30)
else:
    print(28)
