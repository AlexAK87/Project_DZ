import sys


def calculator(number1, number2, operation):
    if operation == '/':
        return number1 / number2
    elif operation == '*':
        return number1 * number2
    elif operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2


def number_entered(number):
    try:
        return int(number)
    except Exception:
        while True:
            print('Ошибка ввода числа')
            next_number = input('Введите число еще раз: ')
            return number_entered(next_number)


def operation_check(operation):
    list_operation = ['/', '*', '+', '-']

    if operation in list_operation:
        return operation
    else:
        while True:
            print('Ошибка ввода операции.')
            next_operation = input('Введите операцию еще раз: ')
            return operation_check(next_operation)


while True:
    number1 = input('Введите первое число: ')
    number1 = number_entered(number1)

    operation = input('Введите вид операции: ')
    if operation == '0':
        sys.exit('Работа программы завершена!')
    else:
        operation = operation_check(operation)

    number2 = input('Введите второе число: ')
    if number2 == '0' and operation == '/':
        print('Деление на 0 не возможно!')
        continue
    else:
        number2 = number_entered(number2)

    print(calculator(int(number1), int(number2), operation))
