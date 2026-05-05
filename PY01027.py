n = input().strip()
i = 0
ok = 1

while i < len(n):
    if i + 2 < len(n) and n[i:i+3] == '688':
        i += 3
    elif i + 1 < len(n) and n[i:i+2] == '68':
        i += 2
    elif n[i] == '6':
        i += 1
    else:
        ok = 0
        break

if ok == 0:
    print("NO")
else:
    print("YES")