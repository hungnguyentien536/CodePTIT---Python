import math

for t in range(int(input())):
    n = int(input())
    digit_sum = 0
    temp = n
    while temp > 0:
        digit_sum += temp % 10
        digit_sum *= 10
        temp //= 10
    if math.gcd(n, digit_sum) == 1:
        print("YES")
    else:
        print("NO")