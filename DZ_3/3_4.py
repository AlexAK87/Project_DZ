import random


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
