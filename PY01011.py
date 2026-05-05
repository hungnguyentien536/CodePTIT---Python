from itertools import product

digits = ['0', '2', '4', '6', '8']

t = int(input())

for _ in range(t):
    N = int(input())
    result = []

    for length in [2, 4, 6]:
        half = length // 2

        for p in product(digits, repeat=half):
            if p[0] == '0':  # không cho số bắt đầu bằng 0
                continue

            left = ''.join(p)
            pal = left + left[::-1]
            num = int(pal)

            if num < N:
                result.append(num)

    result.sort()
    print(" ".join(map(str, result)))
    