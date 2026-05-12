n = int(input())
matrix = [[]] * n
for i in range(n):
    matrix[i] = [int(i) for i in input().split()]

sumup = 0
sumdown = 0
for i in range(n):
    for j in range(n):
        if j < n - 1 - i:
            sumup += matrix[i][j]
        elif j > n - 1 - i:
            sumdown += matrix[i][j]

k = int(input())
total = abs(sumup - sumdown)
if total > k:
    print("NO")
else:
    print("YES")
print(total)
#PY02040