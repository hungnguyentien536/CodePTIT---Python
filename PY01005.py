s = input()
k = 0

for char in s:
    if char == "4" or char == "7":
        k += 1

if k == 4 or k == 7:
    print("YES")
else:
    print("NO")    
