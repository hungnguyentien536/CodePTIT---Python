for _ in range(int(input())) :
    n, m, k = [int(i) for i in input().split()]
    x1, x2, x3, ok = 0, 0, 0, 0
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    while x1 < n and x2 < m and x3 < k :
        if a[x1] == b[x2] and b[x2] == c[x3] :
            print(a[x1], end = ' ')
            ok = 1
            x1 += 1
            x2 += 1
            x3 += 1
        elif a[x1] < b[x2]:
            x1 += 1
        elif b[x2] < c[x3]:
            x2 += 1
        elif c[x3] < a[x1]:
            x3 += 1
    if ok == 0:
        print('NO')
    else:
        print()