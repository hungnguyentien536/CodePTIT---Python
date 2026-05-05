a = []
while (len(a) < 10):
    a = a + list(map(int, input().split()))
b = set()
for i in a:
    b.add(i % 42)
print(len(b))