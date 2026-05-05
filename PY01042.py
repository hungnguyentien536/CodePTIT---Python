for t in range (int(input())):
    s = input()
    test = 1
    for i in range (0, len(s) - 1):
        if s[i] != '0' and s[i] != '1' and s[i] != '2':
            test = 0
    if test == 0:
        print("NO")
    else:
        print("YES")        