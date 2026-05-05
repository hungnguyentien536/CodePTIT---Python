for t in range(int(input())):
    s = input()
    n = 0
    for i in s:
        if i.isdigit():
            n += int(i)
    
    x = [i for i in s if not i.isdigit()]
    s = "".join(sorted(x))
    print(s + str(n))
    