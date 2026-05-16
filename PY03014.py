t = int(input())
for _ in range(t):
    s = input()
    lists = []
    x = 1
    for i in s:
        if i == "(":
            lists.append(x)
            print(x, end=" ")
            x += 1
        elif i == ")":
            print(lists[-1], end= " ")
            lists.pop()
    print()
