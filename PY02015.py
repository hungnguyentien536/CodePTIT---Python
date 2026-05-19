while True:
    lists = [int(i) for i in input().split()]
    if lists.count(0) == 4:
        break
    cnt = 0
    while lists.count(lists[0]) != 4:
        tmp = lists.copy()
        for i in range(4):
            lists[i] = abs(tmp[i] - tmp[(i + 1) % 4])
        cnt += 1
    print (cnt)
