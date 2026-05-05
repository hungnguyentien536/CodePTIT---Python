t = int(input())

for _ in range(t):
    s = input()
    res = ""
    for i in range(0, len(s), 2):
        temp = s[i] * int(s[i+1])
        res = res + temp
    print(res)
