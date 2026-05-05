for t in range (int(input())):
    s = input()
    check = 1
    for i in range(2, len(s)):
        if s[i] != s[i - 2]:
            check = 0
    if check == 1:
        print("YES")      
    else:
        print("NO")  