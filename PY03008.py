n = int(input())
m = {}
ok = 1
for k in range(n - 1):
    x, y = [int(i) for i in input().split()]
    if x not in m:
        m[x] = 1
    else:
        m[x] += 1
    if y not in m:
        m[y] = 1
    else:
        m[y] += 1

for i in range(1, n + 1) :
    if not(i in m) or (m[i] != 1 and m[i] != n - 1) :
        ok = 0
        print("No")
        break
if ok == 1 : print("Yes")