def cardinality_check(numbers_dict):
    for n in range(2, 99 + 1):
        for k, i in numbers_dict.items():
            if n % k == 0:
                i += 1
                numbers_dict[k] = i


numbers_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

cardinality_check(numbers_dict)

for k, i in numbers_dict.items():
    print('Числу {} кратно {}'.format(k, i))

