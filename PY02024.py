def mul(s):
    i = 1
    for c in s:
        i *= int(c)
    return i

for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key= lambda s:(mul(s), int(s)))
    print(*a)