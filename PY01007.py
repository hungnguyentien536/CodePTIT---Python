t = int(input())
for _ in range(t):
    n,x,m = map(float, input().split)
    y = 0
    while n < m :
        n = n + n * (x/100)
        y += 1
    print(y)   