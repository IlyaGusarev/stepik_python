# На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит натуральное
# число из отрезка [a;b] с максимальной суммой делителей.

a = int(input())
b = int(input())
total = 0
temp_total = 0
max_num = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
       if i % j == 0:
           temp_total += j
       if temp_total >= total:
           max_num = i
           total = temp_total
    temp_total = 0
print(max_num, total)