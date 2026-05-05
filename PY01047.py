import math
def check(n):
    if n <= 1:
        return "NO"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "NO"
    return "YES"

for t in range (int(input())):
    s = input()
    n = int(s[-4:])
    print(check(n))
