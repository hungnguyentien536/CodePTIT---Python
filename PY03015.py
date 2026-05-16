import sys

input = sys.stdin.readline

def dfs(u, ban, vis, g):
    vis[u] = 1

    for v in g[u]:
        if v != ban and not vis[v]:
            dfs(v, ban, vis, g)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    best = 1
    mx = 1

    for ban in range(1, n + 1):
        vis = [0] * (n + 1)
        cnt = 0

        for i in range(1, n + 1):
            if i != ban and not vis[i]:
                cnt += 1
                dfs(i, ban, vis, g)

        if cnt > mx:
            mx = cnt
            best = ban

    print(best if mx > 1 else 0)