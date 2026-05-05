import itertools

s = input()
perm = itertools.permutations(s)

for permutaion in perm:
    for char in permutaion:
        print(char, end="")
    print() 