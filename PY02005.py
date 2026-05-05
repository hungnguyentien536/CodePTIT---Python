n = int(input())
cnt = 0
x = [int(i) for i in input().split()]
for i in range(0, n-1):
    for j in range(1,n):        
        if x[i] > x[j] and i < j:
            cnt +=1
        

print(cnt)