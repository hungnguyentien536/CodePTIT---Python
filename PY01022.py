s = input()
cnt = 0
while(len(s) > 1) :
    n = 0
    for i in s:
        n += ord(i) - ord('0')
    s = str(n)
    cnt += 1
print(cnt)