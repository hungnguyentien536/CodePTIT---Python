from collections import deque
import sys

input = sys.stdin.readline

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)]

t = int(input())

for _ in range(t):
    xa, ya, xb, yb = map(int, input().split())
    n = int(input())

    cells = set()

    for _ in range(n):
        x, y1, y2 = map(int, input().split())
        for y in range(y1, y2 + 1):
            cells.add((x, y))

    q = deque()
    q.append((xa, ya, 0))

    visited = set()
    visited.add((xa, ya))

    ans = -1

    while q:
        x, y, d = q.popleft()

        if (x, y) == (xb, yb):
            ans = d
            break

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if (nx, ny) in cells and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, d + 1))

    print(ans)