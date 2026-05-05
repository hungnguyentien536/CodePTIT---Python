n = int(input())
a = [int(i) for i in input().split()]
step = 10**9
x = 0
for i in a:
    y = 0
    for j in a:
        y += abs(i - j)
    if step > y:
        step = y
        x = i
print(step, x)
    