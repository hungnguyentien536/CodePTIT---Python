for t in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    cnt = 0
    tmp = 0
    ch = int(n/2)
    max_val = -1 
    if n == 1:
        print(a[0])
        continue
    
    for i in range(n-1):
        if a[i] == a[i+1]:
            if tmp == 0:
                tmp = 2
            else:
                tmp += 1
        else:
            if tmp > cnt:
                cnt = tmp
                max_val = a[i]  # store the value
            tmp = 0
        
        if tmp > cnt:
            cnt = tmp
            max_val = a[i]  # store the value
    
    if cnt == 0 or cnt < ch:
        print("NO")
    else:
        print(max_val)  # print the value, not the count