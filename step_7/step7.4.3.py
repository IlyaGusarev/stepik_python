# На вход программе подается последовательность целых чисел делящихся на 77, каждое число на отдельной строке. Концом последовательности является любое число не делящееся на 77. Напишите программу, которая выводит члены данной последовательности.

num = int(input())

while num % 7 == 0:
    print(num)
    num = int(input())
