n = int(input())
a = [int(i) for i in input().split()]
a.sort()

for i in range(1, n + 2):
    if i not in a:
        print(i)
        break
    
