n, m = [int(i) for i in input().split()]
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
A = {}
B = {}
for i in a:
    A[i] = 1
for i in b:
    B[i] = 1
    
if A == B:
    print("YES")
else:
    print("NO")