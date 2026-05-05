ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    str = input()
    if str == '0':
        break

    k, s = str.split()
    k = int(k)
    res = ""
    for i in s:
        j= ss.find(i)
        res += ss[(j+k) %28]
    res = res[::-1]
    print(res)