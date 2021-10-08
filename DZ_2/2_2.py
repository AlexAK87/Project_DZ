number = input('Введите число: ')

list_even_numbers = []
list_odd_numbers = []

for i in number:
    if int(i) % 2 == 0:
        list_even_numbers.append(i)
    else:
        list_odd_numbers.append(i)

print(len(list_even_numbers), 'четных числа ({})'.format(','.join(list_even_numbers)))
print(len(list_odd_numbers), 'нечетных числа ({})'.format(','.join(list_odd_numbers)))


