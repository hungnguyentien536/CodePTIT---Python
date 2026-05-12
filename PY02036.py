import math
n = int(input())
lists = sorted([int(i) for i in input().split()])

for i in range(n):
    for j in range(i+1, n):
        if math.gcd(lists[i], lists[j]) == 1:
            print(lists[i], lists[j], sep=" ")
           