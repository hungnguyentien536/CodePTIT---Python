for _ in range (int(input())):
    n = input()
    l = len(n)
    sums= 0
    for i in range(0, l):
        sums += int(n[i])
    s = str(sums)
    if s == s[::-1] and len(s) > 1:
        print("YES")
    else:
        print("NO")   
