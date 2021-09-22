# Напишите программу, которая считывает целое положительное число n от 1 до 9 включительно и выводит значение числа n + nn + nnn.

num = int(input())

print(num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))
