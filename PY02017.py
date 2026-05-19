for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for x in d:
        if d[x] % 2 == 1:
           print(x)
           break
    