import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


def numSum(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n = n // 10  
    return digit_sum    

t = int(input())
for _ in range(t):
    inputs = input().split()

    a = int(inputs[0])
    b = int(inputs[1])

    n = math.gcd(a, b)  
    x = numSum(n)
     
    if isPrime(x):
        print("YES")
    else:
        print("NO")