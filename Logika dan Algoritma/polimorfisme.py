from abc import ABCMeta, abstractmethod

#kelas abstrak
class DuaDimensi184220028(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
            pass

#kelas Segiempat turunan dari kelas Dua Dimensi
class Segiempat(DuaDimensi184220028):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
        #mengimplementasikan metode luas()
    def luas(self):
        return self.panjang * self.lebar

#kelas Segitiga turunan dari kelas DuaDimensi
class Segitiga(DuaDimensi184220028):
    def __init__ (self, a, t):
        self.alas = a
        self.tinggi = t
    #mengimplementasikan metode luas()
    def luas(self):
        return (self.alas * self.tinggi) / 2

#kelas lingkaran turunan dari kelas DuaDimensi
class Lingkaran(DuaDimensi184220028):
    def __init__ (self, r):
        self.radius = r
    #mengimplementasikan metode luas()
    def luas(self):
        import math
        return math.pi* (self.radius ** 2)
    
#membuat list kosong
mylist = []
print(mylist)

#menambahkan objek Segiempat ke dalam mylist
mylist.append(Segiempat(10, 8))
print(mylist)

#menambahkan objek Segitiga ke dalam mylist
mylist.append(Segitiga(3, 5))
print(mylist)

#menambahkan objek Lingkaran ke dalam mylist
mylist.append(Lingkaran(4))
print(mylist)

#menulusuri seluruh elemen mylist, kemudian memanggil metode luas() dari setiap objek yang ditelurusi
for obj in mylist:
    if not issubclass(obj.__class__, DuaDimensi184220028):
        raise TypeError('Objek harus turunan dari Dua Dimensi')
    if isinstance(obj, Segiempat):
        print('Luas Segiempat = ', end='')
    elif isinstance(obj, Segitiga):
        print('Luas Segitiga = ', end='')
    else:
        print('Luas lingkaran = ', end='')
    print(obj.luas())


