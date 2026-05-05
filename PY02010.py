while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for _ in range(n):
        i = int(input())
        a.append(i)
        x = min(a)
        y = max(a)
        
    if x == y:
        print("BANG NHAU")
    else:
        print(x, y)
