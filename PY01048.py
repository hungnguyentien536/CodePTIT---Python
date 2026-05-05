import math

for _ in range(int(input())):
    n = int(input())
    count = 0
    x = 2 * n
    for k in range(2, int(math.sqrt(x)) + 1):
        if x % k == 0:
            if (x // k - k + 1) % 2 == 0:
                count += 1
    print(count)