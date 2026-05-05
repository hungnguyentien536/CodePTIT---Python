def check(n, adj, u, v, x):
    q, visited = [u], {u, x}
    for curr in q:
        if curr == v: return True
        for nxt in adj[curr]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return False

t_str = input().strip()
if t_str:
    for _ in range(int(t_str)):
        n, m, u, v = map(int, input().split())
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            adj[x].append(y)
        
        ans = 0
        for i in range(1, n + 1):
            if i != u and i != v:
                if not check(n, adj, u, v, i):
                    ans += 1
        print(ans)