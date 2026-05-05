import re

for t in range(int(input())):
    print(min(int(i) for i in re.findall(r'\d+', input())))