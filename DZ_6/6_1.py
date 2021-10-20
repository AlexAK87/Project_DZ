import sys
import random

"""Версии
3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)]
Windows 10 Pro 64-разрядная операционная система"""


"""Задание 1 3 урока"""
def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)

def cardinality_check(numbers_dict):
    for n in range(2, 99 + 1):
        for k, i in numbers_dict.items():
            if n % k == 0:
                i += 1
                numbers_dict[k] = i

def result_show3_1():
    numbers_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    cardinality_check(numbers_dict)

    for k, i in numbers_dict.items():
        print('Числу {} кратно {}'.format(k, i))

    return locals()

"""Задание 4 3 урока"""
def result_show_3_4():
    list1 = []
    for i in range(15):
        list1.append(random.randrange(1, 50))

    print(list1)

    list1.sort()
    result = {}
    for n in list1:
        if result.get(n) is None:
            result[n] = 1
        else:
            m = result.get(n)
            m += 1
            result[n] = m

    max_k = 0
    max_i = 0

    for k, i in result.items():
        if i > max_i:
            max_i = i
            max_k = k

    print(result)
    print('Число {} встречается чаще всего.'.format(max_k))

    return locals()


print('result_show3_1')
show_size(result_show3_1())

print('result_show_3_4')
show_size(result_show_3_4())

print(sys.version)