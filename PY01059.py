for _ in range(int(input())):
    s = input()
    sums= 0
    mul= 0
    for i in range(len(s)):
        if i % 2 == 0:
            sums += int(s[i])
        else:
            if s[i] != '0':
                if mul == 0:
                    mul = int(s[i])
                else:
                    mul *= int(s[i])
    print (str(sums) + " " + str(mul))
    