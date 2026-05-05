import math
def prime(n):
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2

lists = [0 , 2]
k = 3
while (len(lists) <= 1001):
    if(prime(k)):
        lists += [k]
    k += 2

n, x = [int (i) for i in input().split()]
for i in range(n + 1):
    x += lists[i]
    print(x, end=" ")