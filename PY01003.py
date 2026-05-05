t = int(input())
for _ in range(t):
    n = int(input())
    k = 10
    while n >= k:
        r= n % k
        h = k//2
        if r >= h :
            n = n + k - r
        else :
            n = n -r
        k *= 10
    print(n)

