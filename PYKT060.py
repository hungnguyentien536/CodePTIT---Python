import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

# ma trận kề
adj = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = adj[v][u] = 1

# color[i] = số lần đổi trạng thái đỉnh i mod 2
color = [-1] * (n + 1)

for s in range(1, n + 1):
    if color[s] != -1:
        continue

    color[s] = 0
    q = deque([s])

    while q:
        u = q.popleft()

        for v in range(1, n + 1):
            if u == v:
                continue

            need = color[u] ^ (1 - adj[u][v])

            if color[v] == -1:
                color[v] = need
                q.append(v)
            elif color[v] != need:
                print("NO")
                sys.exit()

print("YES")