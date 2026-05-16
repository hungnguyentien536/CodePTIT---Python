import sys

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def solve(a):
    n = len(a)

    pre = [-1] * n
    nxt = [n] * n

    pos = {}

    for i, x in enumerate(a):
        pre[i] = pos.get(x, -1)
        pos[x] = i

    pos.clear()

    for i in range(n - 1, -1, -1):
        x = a[i]
        nxt[i] = pos.get(x, n)
        pos[x] = i

    stack = [(0, n - 1)]

    while stack:
        l, r = stack.pop()

        while l < r:
            ok = False

            for d in range((r - l + 1) // 2 + 1):
                i = l + d

                if pre[i] < l and nxt[i] > r:
                    stack.append((l, i - 1))
                    l = i + 1
                    ok = True
                    break

                j = r - d

                if pre[j] < l and nxt[j] > r:
                    stack.append((j + 1, r))
                    r = j - 1
                    ok = True
                    break

            if not ok:
                return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print("YES" if solve(a[:-1]) and solve(a[1:]) else "NO")