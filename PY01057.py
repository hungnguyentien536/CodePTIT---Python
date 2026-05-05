import math
def prime(x):
    if x < 2: 
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

def solve(s):
    if len(s) <= 2:
        return "NO"
    for i in range (2, len(s)):
        if prime(i): 
            if not prime(int(s[i])):
                return "NO"
        if not prime(i): 
            if prime(int(s[i])):
                return "NO"       
    return "YES"
        
    

for _ in range(int(input())):
    n = input()
    print(solve(n))
    
