def solve(n):
    if n <= 1:
        return 'NO'
    for i in range(2, n):
        if n % i == 0:
            return 'NO'
    return 'YES'

for _ in range (int(input())):
    n = input()
    l = len(n)
    sums= 0
    for i in range(0, l):
        sums += int(n[i])
    print(solve(sums))
