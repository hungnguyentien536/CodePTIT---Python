a, b, m = map(int, input().split())

if m > 3:
    print(sum(1 for i in [0, 1] if a <= i <= b))
elif m == 3:
    print(sum(1 for i in [0, 1, 6643, 1422773] if a <= i <= b))
elif m == 2:
    res = {0, 1} if a <= 0 <= b else {1} if a <= 1 <= b else set()
    for i in range(1, 1024):
        s = bin(i)[2:]
        r = s[::-1]
        for x in [int(s + r, 2), int(s + '0' + r, 2), int(s + '1' + r, 2)]:
            if a <= x <= b:
                res.add(x)
    print(len([x for x in res if a <= x <= b]))
else:
    print(0)