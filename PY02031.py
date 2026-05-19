import math
def prime(s):
    if s < 2:
        return 0
    for i in range(2, int(math.sqrt(s))+ 1):
        if s % i == 0:
            return 0
    return 1

n, m = [int(i) for i in input().split()]
for i in range(n):
    lists = [prime(int(i)) for i in input().split()]
    print(*lists)
