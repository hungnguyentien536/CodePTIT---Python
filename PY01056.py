import math
def solve(s):
    for i in range (len(s)):
        if i % 2 != int(s[i]) % 2:
            return "NO"
        
    x = sum(int(i) for i in s)
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return "NO"
    return "YES"



for _ in range(int(input())):
    n = input()
    print(solve(n))
    