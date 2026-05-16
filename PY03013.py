import sys

def count_digit(n, d):
    if n < 0:
        return 0

    res = 0
    factor = 1

    while factor <= n:
        lower = n % factor
        cur = (n // factor) % 10
        higher = n // (factor * 10)

        if d != 0:
            if cur > d:
                res += (higher + 1) * factor
            elif cur == d:
                res += higher * factor + lower + 1
            else:
                res += higher * factor
        else:
            if higher != 0:
                if cur > 0:
                    res += (higher - 1 + 1) * factor
                elif cur == 0:
                    res += (higher - 1) * factor + lower + 1
                else:
                    res += (higher - 1) * factor

        factor *= 10

    return res

def solve(a, b):
    if a > b:
        a, b = b, a

    ans = []
    for d in range(10):
        ans.append(count_digit(b, d) - count_digit(a - 1, d))

    return ans

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(*solve(a, b))