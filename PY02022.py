import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]
dicts = {}
for i in range(len(a)):
    if prime(a[i]):
        if a[i] in dicts:
            dicts[a[i]] += 1
        else:
            dicts[a[i]] = 1
for i in dicts:
    print(str(i) + " " + str(dicts[i]))
