n = int(input()) + 1
a = [int (i) for i in input().split()] + [-1]
ans = 0
x = 0
k = max(a)
for i in range(n):
    if a[i] == k:
        x += 1
    else:
        ans = max(x,ans)
        x = 0

print (ans)