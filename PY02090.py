import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    a = [list(map(int, input().strip())) for _ in range(n)]

    if n > m:
        a = list(zip(*a))
        n, m = m, n

    ans = 0
    col = [0] * m

    for top in range(n):
        col = [0] * m

        for bottom in range(top, n):
            row = a[bottom]

            for j in range(m):
                col[j] += row[j]

            l = 0
            s = 0

            for r in range(m):
                s += col[r]

                while s > k:
                    s -= col[l]
                    l += 1

                if s == k:
                    ans += 1
                    x = l

                    while x < r and col[x] == 0:
                        ans += 1
                        x += 1

    print(ans)