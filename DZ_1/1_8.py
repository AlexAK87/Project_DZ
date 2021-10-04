import sys

while True:
    year = input('Введите год: ')

    if year == 'exit':
        sys.exit('Работа программы завершена')
    elif int(year) % 400 == 0:
        print("{} високосный".format(year))
    elif int(year) % 100 == 0:
        print("{} не високосный".format(year))
    elif int(year) % 4 == 0:
        print("{} високосный".format(year))
    else:
        print("{} не високосный".format(year))