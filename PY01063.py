for t in range(int(input())):
    s = input()
    n = input()
    count= 0
    substr = s.find(n)
    while substr != -1:
        count += 1
        substr = s.find(n, substr + len(n))
    print(count)