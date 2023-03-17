from abc import ABCMeta, abstractmethod

#kelas abstrak
class DuaDimensi184220028(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
            pass

#kelas Segiempat turunan dari kelas DuaDimensi
class Segiempat(DuaDimensi184220028):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    #mengimplementasikan metode luas()
    def luas(self):
        return self.panjang * self.lebar

#kelas Segitiga turunan dari kelas DuaDimensi
class Segitiga(DuaDimensi184220028):
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    #mengimplementasikan metode luas()
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
#kelas lingkaran turunan dari kelas DuaDimensi
class Lingkaran(DuaDimensi184220028):
    def __init__ (self, r):
        self.radius = r
    #mengimplementasikan metode Luas()
    def luas(self):
        import math
        return math.pi * (self.radius ** 2)

#obj = DuaDimensi184220028()
#print(obj)
obj1 = Segiempat(10, 8).luas()
print(obj1)
obj2 = Segitiga(3, 5).luas()
print(obj2)
obj3 = Lingkaran(4).luas()
print(obj3)