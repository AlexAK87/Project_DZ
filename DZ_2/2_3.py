
number = input('Введите число: ')

list_number = []

for i in number:
    list_number.append(i)

list_number.reverse()
print('Введенное число в обратном порядке {}'.format(''.join(list_number)))

