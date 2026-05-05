def solve(n, source, aux, target):
    if n <= 0:
        return
    if n == 1:
        print(f"{source} -> {target}")
        return
    solve(n - 1, source, target, aux)
    print(f"{source} -> {target}")
    solve(n - 1, aux, source, target)

n = int(input())
solve(n, 'A', 'B', 'C')