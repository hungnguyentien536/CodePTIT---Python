n = int(input())
cnt = 0
x = [int(i) for i in input().split()]
for i in range(1, n):
    if x[i] != x[i-1]:
        cnt += 1

print(cnt)