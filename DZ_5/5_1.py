from collections import namedtuple
from statistics import mean

list_company = namedtuple('list_company', 'name_company profit_list avg')

lst = []
for i in range(int(input('Введите количество компаний: '))):
    arg = input('Введите в строку имя и поквартальную прибыль через пробел:\n').split()
    lst.append(list_company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name_company} \t\tСредняя прибыль за год: {i.avg}')

print('_' * 70, '\n')

print('Компании с прибылью меньше средней:')
for i in lst:
    if i.avg < avg:
        print(i.name_company)

print('Компании с прибылью больше средней:')
for i in lst:
    if i.avg > avg:
        print(i.name_company)