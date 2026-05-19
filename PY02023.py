def sort_key(s):
    digit_sum = sum(int(i) for i in s)
    numeric_value = int(s)
    return (digit_sum, numeric_value)

for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=sort_key)
    print(*a)