def check(a,b):
    if a == b:
        return "YES"
    return "NO"
for t in range (int(input())):
    a = sorted((input()))
    b = sorted((input()))
    print("Test " + str(t + 1) + ": " + check(a,b))
