for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        v_min, v_max = min(a[i], a[i+1]), max(a[i], a[i+1])
        while v_max > 2 * v_min:
            ans += 1
            v_min *= 2
    print(ans)