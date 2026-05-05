import math
def prime(n):
    for i in range(2, int(math.sqrt(int(n))) + 1):
        if n % i == 0:
            return False
    return n > 1

def perfect(s):
    for i in s:
        if not prime(int(i)):
            return "No"
    sums = sum([int(i) for i in s])
    if not prime(sums):
        return "No"
    if not prime(int(s)) or not prime(int(s[::-1])):
        return "No"
    return "Yes"

for t in range(int(input())):
    n = input()
    print(perfect(n))