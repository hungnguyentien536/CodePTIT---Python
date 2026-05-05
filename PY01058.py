import math
def prime(x):
    if x < 2: 
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

def solve(s):
    if len(s) <= 3:
        return "NO"
    x = int(s[-4:])
    if prime(x):
        return "YES"
    return "NO"
        
for _ in range(int(input())):
    n = input()
    print(solve(n))
    
