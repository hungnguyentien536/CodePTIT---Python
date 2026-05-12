from itertools import product

n = int(input())

digits = '2357'

for length in range(4, n + 1):
    for p in product(digits, repeat=length):
        s = ''.join(p)

        if s[-1] == '2':
            continue

        if all(d in s for d in digits):
            print(s)