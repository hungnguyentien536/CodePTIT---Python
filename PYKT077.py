from datetime import datetime

n, m = map(int, input().split())

monhoc = {}

for _ in range(n):
    ma = input().strip()
    ten = input().strip()
    monhoc[ma] = ten

ds = []

for i in range(1, m + 1):
    ma, ngay, gio, nhom = input().split()
    maca = f"T{i:03d}"

    dt = datetime.strptime(ngay + " " + gio, "%d/%m/%Y %H:%M")

    ds.append([dt, gio, ma, maca, ngay, nhom])

ds.sort(key=lambda x: (x[0], x[2]))

for x in ds:
    _, gio, ma, maca, ngay, nhom = x
    print(maca, ma, monhoc[ma], ngay, gio, nhom)