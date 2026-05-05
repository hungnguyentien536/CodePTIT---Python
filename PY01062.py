import math
def prime(x):
    if x < 2: 
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

def solve(s):
    if len(s) <= 2 or not prime(len(s)):
        return "NO"
    np = 0
    p = 0
    for i in range (0, len(s)):
        if prime(int(s[i])):
            p += 1
        else:
            np += 1
    if np >= p:
        return "NO"
    return "YES"
        
    

for _ in range(int(input())):
    n = input()
    print(solve(n))
    
