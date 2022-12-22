# Реализуйте алгоритм перемешивания списка.

import datetime
def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)

a = [1,2,3,4,5,6]
print(a)
random_int(len(a)-1)
for x in range(len(a)-1,-1,-1):
    y = random_int(x+1)
    a[x],a[y] = a[y],a[x]
print(a)
