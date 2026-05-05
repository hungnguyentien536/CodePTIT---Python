import itertools

n, k = [int(i) for i in input().split()]
lists = sorted(list({int(i) for i in input().split()}))
comb = itertools.combinations(lists,k)

for combination in comb:
    for number in combination:
        print(number, end=" ")
    print() 