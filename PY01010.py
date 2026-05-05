t = int(input().strip())

for _ in range(t):
    N = input().strip()
    
    if N[0] == N[-2] and N[1] == N[-1]:
        print("YES")
    else:
        print("NO")