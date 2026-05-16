import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

a = [tuple(map(int, input().split())) for _ in range(n)]


a.sort(key=lambda p: (p[0], -p[1]))

lis = []

for _, y in a:
    pos = bisect_left(lis, y)

    if pos == len(lis):
        lis.append(y)
    else:
        lis[pos] = y

print(len(lis))