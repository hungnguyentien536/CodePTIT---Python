def solve(n1, n2, a, b):
    n1 = int(n1.replace(a, b))
    n2 = int(n2.replace(a, b))
    return n1 + n2
    
for t in range(int(input())):
    n, p = [int(i) for i in input().split()]
    l = str(min(n,p))
    h = str(max(n,p))
    x1 = input()
    if len(x1.split()) > 1:
        x1, x2 = x1.split()
    else: x2 = input()
    print(solve(x1, x2, h, l), solve(x1, x2, l, h))
    