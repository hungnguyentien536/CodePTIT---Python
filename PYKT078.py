t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    mx = max(a)

    pos = a.index(mx)
    a.insert(pos, m)

    am = [x for x in a if x < 0]
    duong = [x for x in a if x >= 0]

    res = am + duong

    print(*res)