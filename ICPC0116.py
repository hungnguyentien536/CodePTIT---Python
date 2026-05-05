for t in range (int(input())):
    s = input()
    rev = s[::-1]
    start = int(rev) %10
    ends = int(s) %10
    if start != ends:
        print('NO')
    else:
        print("YES")