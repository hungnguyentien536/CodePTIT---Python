while True:
    n = int(input())
    cnt = 1
    if n == 0:
        break
    
    while(n != 1):
        if n % 2 == 0:
            n /= 2
            cnt +=1
        else:
            n = n*3 + 1
            cnt += 1
    
    if n == 1:
        print(cnt)
        continue
    
