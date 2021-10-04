import sys


def searching_letter(number, case_letter):
    if case_letter == 'Верхний':
        print(chr(number))
    elif case_letter == 'Нижний':
        print(chr(number + 32))
    else:
        print('Не выбран регистр буквы. Операция прервана')


while True:
    case_letter = input('В каком регистре вывести букву? Варинаты Верхний\Нижний: ')
    print('Для выхода введите exit!')
    number = input('Введите номер буквы от 65 до 90 ')

    if number == 'exit':
        sys.exit('Поиск прерван')
    elif int(number) < 65 or int(number) > 90:
        print('Введите число в диапозоне 65-90!')
    else:
        searching_letter(number, case_letter)
