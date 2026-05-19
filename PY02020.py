n = int(input())
a = [float(i) for i in input().split()]
l = min(a)
h = max(a)

lst = []
for i in range(len(a)):
    if a[i] != l and a[i] != h:
        lst.append(a[i])
        
avg = sum(lst) / len(lst)
print(f"{avg:.2f}")