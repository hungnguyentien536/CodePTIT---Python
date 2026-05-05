for _ in range (int(input())):
    n = input()
    l = len(n)
    sums= 1
    for i in range(0, l):
        if n[i] != '0':
            sums *= int(n[i])
    print(sums) 
