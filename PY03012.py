students = []
for n in range (int(input())):
    name = input()
    c, t = [int(i) for i in input().split()]
    students.append((name, c, t))

students.sort(key=lambda x: (-x[1], x[2], x[0]))


for name, c, t in students:
    print(name, c, t)