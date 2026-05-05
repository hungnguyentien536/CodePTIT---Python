import math
def prime(n):
    for i in range(2, int(math.sqrt(int(n))) + 1):
        if n % i == 0:
            return False
    return n > 1

for t in range(int(input())):
    used = []
    n = int(input())
    for i in range(13, n):
        num = str(i)
        if int(num[::-1]) < n and num != num[::-1] and prime(int(num)) and prime(int(num[::-1])) and num not in used:
            print(num, num[::-1], end=' ')
            used += [num, num[::-1]]
    print()