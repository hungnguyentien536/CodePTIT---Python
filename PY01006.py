t = int(input())

for _ in range(t):
    s = input()

    for char in s:
        if char != "4" and char != "7":
            print ("NO")
            break
    else:
        print("YES")   

