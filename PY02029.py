n, k = [int (i) for i in input().split()]
a = [int (i) for i in input().split()]
m = {}
ans = x = check = k = 0
for i in a:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
    x = max(m[i], x)

for i in range(1, n + 1):
    if i in m and m[i] != x and m[i] > k:
        check = 1
        k = max(k, m[i])
        ans = i

if check == 0:
    print("NONE")
else:
    print(ans)