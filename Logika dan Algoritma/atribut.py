class PersegiPanjang184220028:
    counter = 0
    def __init__(self, p, l):
        PersegiPanjang184220028.counter += 1
        self.panjang = p
        self.lebar = l
    def ubahPanjang(self, p):
        self.panjang = p
    def ubahLebar(self, l):
        self.lebar = l
    def hitungLuas(self):
        return self.panjang * self.lebar
    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)
    def cetakLuas(self):
        print('Luas persegi panjang = %.2f' % self.hitungLuas())
    def cetakkeliling(self):
        print('Keliling persegi panjang=% .2f' % self.hitungKeliling())

obj1 = PersegiPanjang184220028(20, 15)
obj2 = PersegiPanjang184220028(10, 8)
obj3 = PersegiPanjang184220028(7, 5)
print(PersegiPanjang184220028.counter)
print(obj1.counter)
print(obj2.counter)
print(obj3.counter)
obj4 = PersegiPanjang184220028(12, 9)
print(PersegiPanjang184220028.counter)
print(obj1.counter, obj2.counter, obj3.counter, obj4.counter)