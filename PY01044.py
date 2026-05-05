a = [i.lower() for i in input().split()]
b = [i.lower() for i in input().split()]
x1, x2, x3 = {}, {}, {}

for i in a:
    x1[i] = 1
    x2[i] = 1
for i in b:
    x1[i] = 1
    x3[i] = 1
    
for i in sorted(x1):
    print(i, end=' ')
print()

for i in sorted(x2):
    if i in x3:
        print(i, end=' ')