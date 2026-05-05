BASE = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for t in range(int(input())):
    n, b = map(int, input().split())
    
    if n == 0:
        print('0')
        continue
    
    res = ''
    while n > 0:
        res = BASE[n % b] + res
        n //= b
    
    print(res)