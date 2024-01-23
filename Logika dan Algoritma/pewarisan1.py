class Kota:
    def __init__(self,namakota,namakecamatan):
        self.namakota = namakota
        self.namakecamatan = namakecamatan
    
class kecamatan (Kota):
    def ULBI (self):
        print ("Lokasi ULBI :")

alamat = kecamatan("Bandung", "Sukasari")

alamat.ULBI()    
print (alamat.namakota)
print (alamat.namakecamatan)
