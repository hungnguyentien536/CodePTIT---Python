import sys
sys.setrecursionlimit(10**7)

sign = ['+', '-']
isOK = False
s = ""

def is_correct():
    try:
        x = int(s[0:2])
        y = int(s[5:7])
        z = int(s[10:12])
    except:
        return False

    if x < 10 or y < 10 or z < 10:
        return False

    if s[3] == '+':
        return x + y == z
    else:
        return x - y == z


def Try(i):
    global isOK, s

    if isOK:
        return

    if i == len(s):
        if is_correct():
            isOK = True
            print(s)
        return

    if s[i] == '?':
        if i == 3:
            for op in sign:
                s = s[:i] + op + s[i+1:]
                Try(i + 1)
        else:
            for d in range(10):
                s = s[:i] + str(d) + s[i+1:]
                Try(i + 1)
        s = s[:i] + '?' + s[i+1:]
    else:
        Try(i + 1)


def test_case():
    global isOK, s
    isOK = False
    s = input()

    for ch in s:
        if ch in ['*', '/']:
            print("WRONG PROBLEM!", end="")
            return

    Try(0)

    if not isOK:
        print("WRONG PROBLEM!", end="")



t = int(input())
for _ in range(t):
    test_case()
    print()