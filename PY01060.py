for _ in range(int(input())):
    s = input()
    sums= 0
    mul= 1
    for i in range(len(s)):
        if i % 2 != 0:
            sums += int(s[i])
        else:
            if s[i] != '0':              
                mul *= int(s[i])
    print (str(mul) + " " + str(sums))
    