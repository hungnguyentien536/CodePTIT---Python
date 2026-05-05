def solve(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in range(0, len(s)):
        if int(s[i]) % 2 == 1:
            return False
    return True    

for t in range (int(input())):
    n = int(input())
    for i in range (22, n, 22):
        if solve(str(i)):
            print(i, end =' ')
    print()        