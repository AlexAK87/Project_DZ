import random


list1 = []
for i in range(15):
    list1.append(random.randrange(1, 50))

print(list1)
mn = min(list1)
mx = max(list1)
imn = list1.index(mn)
imx = list1.index(mx)
print('list1[%d]=%d list1[%d]=%d' % (imn+1, mn, imx+1, mx))
list1[imn], list1[imx] = list1[imx], list1[imn]
print(list1)