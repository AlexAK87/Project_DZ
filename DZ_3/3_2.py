list1 = [i for i in range(1, 15)]
list2 = []

for i in list1:
    if i % 2 == 0:
        list2.append(list1.index(i))

print(list2)