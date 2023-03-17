#Cara mendefinisikan class
# class NamaClass: #Format Camel Case

#     def __init__(self,nama_attribute1,nama_attribute2): #(__init__ = method)
#         self.nama_attribute1 = nama_attribute1
#         self.nama_attribute2 = nama_attribute2

#     def nama_method(self):
#         return #tulis fungsinya



# class Mobil:
#     def __init__(self,brand,harga): #(__init__ = method)
#         self.brand = brand
#         self.harga = harga

# #kendaraan1 = objek (object) ; Mobil(‘TOYOTA’,1000) = kelas (class)
# kendaraan1 = Mobil('TOYOTA',500)
# print(kendaraan1.brand)
# print(kendaraan1.harga)

# kendaraan2 = Mobil('MITSUBISHI',1000)
# print(kendaraan2.brand)
# print(kendaraan2.harga)

# kendaraan3 = Mobil('BMW',12000)
# print(kendaraan3.brand)
# print(kendaraan3.harga)

# class Mobil:

#     def __init__(self,brand,harga): #(__init__ = method)
#     # self.brand = brand
#     # self.harga = harga

# kendaraan1 = Mobil('TOYOTA',500)
# print(kendaraan1.brand)
# print(kendaraan1.harga)

# kendaraan2 = Mobil('MITSUBISHI',1000) 
# print(kendaraan2.brand)
# print(kendaraan2.harga)

# kendaraan3 = Mobil('BMW',12000)
# print(kendaraan3.brand)
# print(kendaraan3.harga)


# class Buah:
    
#     penjual = 'Pak Imron' # ini class object attribute
#     def __init__(self,nama_buah,harga):
#         self.nama_buah = nama_buah
#         self.harga = harga
#     jenis_buah = 'Pisang Ambon' #ini class object attribute

# fruit1 = Buah('Pisang',10000)
# print('Nama buah =',fruit1.nama_buah)
# print('Harga buah =',fruit1.harga)
# print('Nama penjual buah =',fruit1.penjual)
# print('Jenis Pisang =',fruit1.jenis_buah)

# class Karyawan():
#     jumlah_karyawan=0
#     def __init__(self,nama,jobdesk,lama_bekerja):
#         self.nama = nama
#         self.jobdesk = jobdesk
#         self.lama_bekerja = lama_bekerja
#         Karyawan.jumlah_karyawan +=1

#     def total_karyawan(self):
#         print('Total Karyawan =', Karyawan.jumlah_karyawan)

#     def detail_karyawan(self):
#         print('Nama karyawan :', self.nama)
#         print('Jobdesk karyawan :', self.jobdesk)
#         print('Lama bekerja :', self.lama_bekerja)

# # membuat objek
# karyawan1 = Karyawan ('Adi', 'salesman', '2 bulan')
# karyawan2 = Karyawan ('Susi', 'kadiv HR','2 tahun')
# karyawan3 = Karyawan ('Budi', 'Marketing', '10 bulan')
# karyawan4 = Karyawan ('Tuti', 'Manager', '4 tahun')
# karyawan5 = Karyawan ('Santoso', 'Sekretaris', '5 tahun')

# # mengakses attribut objek
# karyawan1.detail_karyawan()
# karyawan2.detail_karyawan()
# karyawan3.detail_karyawan()
# karyawan4.detail_karyawan()
# karyawan5.detail_karyawan()
# Karyawan.total_karyawan(Karyawan)

# #latsol
class belanja:
    jumlahbelanja = 0
    def __init__(self,namabarang,jumlahbarang,harga,totalharga):
        self.namabarang = namabarang
        self.jumlahbarang = jumlahbarang
        self.harga = harga
        self.totalharga = totalharga
        belanja.jumlahbelanja += 1
    def TotalBeli(self):
        print("Total belanja =", belanja.jumlahbelanja)
    def detailbelanja(self):
        print("Nama Barang =", self.namabarang)
        print("Jumlah Barang =", self.jumlahbarang)
        print("Harga =", self.harga)
        print("Total Harga =", self.totalharga)
barang1 = belanja("Sepatu",1,"Rp. 35.000","Rp. 35.000")
barang2 = belanja("Kemeja",4,"Rp. 2.500.000","Rp. 10.000.000")
barang3 = belanja("Binder B5",2,"Rp. 32.000","Rp. 64.000")
barang1.detailbelanja()
barang2.detailbelanja()
barang3.detailbelanja()
belanja.TotalBeli(belanja)

class data:
    jumlahmahasiswa = 0
    def __init__(self,nama,npm,prodi):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        data.jumlahmahasiswa += 1
    def Totalmahasiswa(self):
        print("Total Mahasiswa =", data.jumlahmahasiswa)
    def detaildata(self):
        print("Nama Mahasiswa =", self.nama)
        print("NPM =", self.npm)
        print("Prodi =", self.prodi)
data1 = data("Dewi Ratnasari",123456789,"Sains Data")
data2 = data("Budi Susanto",234567890,"Sains Data")
data3 = data("Dewi Kartika",345678901,"Sains Data")
data4 = data("Muhamad David",456789012,"Bisnis Digital")
data5 = data("Christian Bambang",567890123,"Bisnis Digital")
data6 = data("Sandra Kusumawati",678901234,"Bisnis Digital")
data1.detaildata()
data2.detaildata()
data3.detaildata()
data4.detaildata()
data5.detaildata()
data6.detaildata()
data.Totalmahasiswa(data)

class kebutuhan:
    jumlahkebutuhan = 0
    def __init__(self,namakebutuhan,tipekebutuhan):
        self.namakebutuhan = namakebutuhan
        self.tipekebutuhan = tipekebutuhan
        kebutuhan.jumlahkebutuhan += 1
    def Totalkebutuhan(self):
        print("Banyaknya Kebutuhan Saya =", kebutuhan.jumlahkebutuhan)
    def detailkebutuhan(self):
        print("Nama Kebutuhan =", self.namakebutuhan)
        print("Tipe Kebutuhan =", self.tipekebutuhan)
data1 = kebutuhan("Makanan","Prioritas")
data2 = kebutuhan("Baju","Penting tapi bukan prioritas")
data3 = kebutuhan("Permen","Tidak penting dan bukan prioritas")
data1.detailkebutuhan()
data2.detailkebutuhan()
data3.detailkebutuhan()
kebutuhan.Totalkebutuhan(kebutuhan)

class menu():
    jumlah_menu = 0
    def __init__(self,nama,asal,peminat):
        self.nama = nama
        self.asal = asal
        self.peminat = peminat
        menu.jumlah_menu += 1
    def banyak_menu(self):
        print("Banyaknya menu yang tersedia :", menu.jumlah_menu)
    def detail_menu(self):
        print("Nama menu: ", self.nama)
        print("Asal menu: ", self.asal)
        print("Banyaknya peminat: ", self.peminat)
c1 = menu("Nasi Padang","Padang","Banyak")
c2 = menu("Rendang","Padang","Banyak")
c1.detail_menu()
c2.detail_menu()
menu.banyak_menu(menu)

class Produk:
    jumlah_produk = 0
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        Produk.jumlah_produk += 1
    def berapa_jumlah(self):
        print("Total Produk =", Produk.jumlah_produk)
    def detail_produk(self):
        print("Nama =", self.nama)
        print("Harga =", self.harga)
produk1 = Produk("Tissue", 26000)
produk2 = Produk("Air Mineral", 3000)
produk3 = Produk("Roti",2000)
produk1.detail_produk()
produk2.detail_produk()
produk3.detail_produk()
Produk.berapa_jumlah(Produk)

class no6:
    def __init__(self, nama, bahasa, pemimpin):
        self.nama = nama
        self.bahasa = bahasa
        self.pemimpin = pemimpin
    alatmusik_khas = "Angklung"
detailno6 = no6("Bandung","Sunda","Ridwan Kamil")
print("Ibu Kota Jawa Barat =", detailno6.nama)
print("Bahasa Daerah =", detailno6.bahasa)
print("Nama Gubernur =", detailno6.pemimpin)
print("Alat Musik Khas =",detailno6.alatmusik_khas)

class no7:
    def __init__(self, brand, harga):
        self.brand = brand
        self.harga = harga
    nama_pemilik = "Fajar"
    storage = "6 GB"
detailno7 = no7("Samsung",10000)
print("Brand HP =", detailno7.brand)
print("Harga HP =", detailno7.harga)
print("Nama Pemilik =", detailno7.nama_pemilik)
print("Storage =",detailno7.storage)

class JamTangan:
    def __init__(self,brand,price,warna):
        self.brand = brand
        self.price = price
        self.warna = warna
Aksesoris = JamTangan("ROLEX",1200,"Silver")
print('Brand HP =',Aksesoris.brand)
print('Price =',Aksesoris.price)
print('Warna =',Aksesoris.warna)
    
class Band:
    def __init__(self,namaband,genre,asal,label,personil,tophits):
        self.namaband = namaband
        self.genre = genre
        self.asal = asal
        self.label = label
        self.personil = personil
        self.tophits = tophits
Detail_band = Band("Rocket Rockers","Indonesian Indie","Bandung","Sony Music Indonesia","Azka, Ozom, Bisma","Ingin Hilang Ingatan")
print("Nama Band =", Detail_band.namaband)
print("Genre =",Detail_band.genre)
print("Asal =",Detail_band.asal)
print("Label =",Detail_band.label)
print("Personil =",Detail_band.personil)
print("Top Hits =",Detail_band.tophits)

class JuicyLucy:
     def __init__(self,genre,label):
        self.genre = genre
        self.label = label
        self.saxophonist = "Zam Zam YM"
        self.vokalis = 'Julian Kaisar'
        self.gitaris = "Denis Ligia"
detialJC = JuicyLucy("Indonesian Pop","E-Motion Entertainment")
print("Genre Band =",detialJC.genre)
print("Label =",detialJC.label)
print("Saxophonist =",detialJC.saxophonist)
print("Vokalis =",detialJC.vokalis)
print("Gitaris =",detialJC.gitaris)