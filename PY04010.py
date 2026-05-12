class ThiSinh:
    tongdiem = 0
    def __init__(self, hoten, ngaysinh, diem1, diem2, diem3):
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.diemtong = diem1 + diem2 + diem3

    def output(self):
        print(self.hoten, self.ngaysinh, "{:.1f}".format(self.diemtong))

ht = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
ts = ThiSinh(ht, ns, d1, d2, d3)
ts.output()
