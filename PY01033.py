import math

lower, upper = [int(i) for i in input().split()]

for i in range(lower, upper + 1):
    for j in range(i + 1, upper + 1 ):
        for k in range(j + 1, upper + 1):
            if (math.gcd(i,j) == 1) and (math.gcd(j,k) == 1) and (math.gcd(k,i) == 1):
                print("(" + str(i) + ", " + str(j) + ", "+ str(k) + ")")