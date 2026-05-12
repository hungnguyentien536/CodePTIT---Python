n = int(input())
matrix = [[]] * n
for i in range(n):
    matrix[i] = [int(i) for i in input().split()]

sumup = 0
sumdown = 0
for i in range(n):
    for j in range(n):
        if i < j:
            sumup += matrix[i][j]
        elif j < i:
            sumdown += matrix[i][j]

k = int(input())
total = abs(sumup - sumdown)
if total > k:
    print("NO")
else:
    print("YES")
print(total)