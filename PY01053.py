for _ in range (int(input())):
    n = input()
    l = len(n)
    sums= 0
    for i in range(0, l):
        sums += int(n[i])
    if sums % 3 == 0:
        print("YES")  
    else:
        print("NO") 
