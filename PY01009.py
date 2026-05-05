s = input().strip()
upper_count = 0
lower_count = 0
for ch in s: 
    if ch.isupper():
        upper_count += 1
    else :
        lower_count += 1
if lower_count >= upper_count:
    print(s.lower())
else:
    print(s.upper())   
