# Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

num1 = int(input())
num2 = int(input())
operation = input()

if operation == '+':
    otv = num1 + num2
    print(otv)
elif operation == '-':
    otv = num1 - num2
    print(otv)
elif operation == '/' and num2 == 0:
    print('На ноль делить нельзя!')
elif operation == '/':
    otv = num1 / num2
    print(otv)
elif operation == '*':
    otv = num1 * num2
    print(otv)
else:
    print('Неверная операция')
