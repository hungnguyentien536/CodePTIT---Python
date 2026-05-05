def solve(n, k):
    mid = pow(2, n - 1)
    if k == mid:
        return n
    elif k < mid:
        return solve(n - 1, k)
    else:
        return solve(n - 1, k - mid)
for _ in range(int(input())):
    n, k = map(int, input().split())
    char = chr(solve(n,k) + ord('A') - 1)
    print(char)
    