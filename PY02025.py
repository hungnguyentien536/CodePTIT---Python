n, m = [int(i) for i in input().split()]
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
A = {}
B = {}
for i in a:
    A[i] = 1
for i in b:
    B[i] = 1
for x in sorted(A):
    if x in B:
        print(x,end=" ")
print()

for x in sorted(A):
    if x not in B:
        print(x,end=" ")
print()

for x in sorted(B):
    if x not in A:
        print(x,end=" ")
print()

