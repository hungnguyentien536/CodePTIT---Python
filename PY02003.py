import bisect

N = 10**18
lists = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            lists.append(i * j * k)  # Use append() instead of +=
            k *= 5
        j *= 3
    i *= 2

lists = sorted(set(lists))  # Remove duplicates and sort

for t in range(int(input())):
    n = int(input())
    idx = bisect.bisect_left(lists, n)  # Binary search instead of linear loop
    if idx < len(lists) and lists[idx] == n:
        print(idx + 1)
    else: 
        print("Not in sequence")