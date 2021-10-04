def calculator(number1, number2, action_performed):
    result = ''
    if action_performed == '*':
        result = str(number1 * number2) + ' Произведение'
    elif action_performed == '+':
        result = str(number1 + number2) + ' Сумма'

    return result


action_performed = input('Выполняемое действие произведение или сумма(Введите * или +): ')

number1 = int(input('Введите первое трехзначное число: '))
number2 = int(input('Введите второе трехзначное число: '))

if len(str(number1)) != 3 or len(str(number2)) != 3:
    print('Введено не трехзначное число, операция прервана')
    number1 = 0
    number2 = 0
else:
    print(calculator(number1, number2, action_performed))
