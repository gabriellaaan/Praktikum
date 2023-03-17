# #komponen dictionary
# kuliah = {
#     'nama:' : 'ulbi',
#     'proditop:' : 'sains data'
# } 
# print (kuliah)

# #membuat dictionary
# #cara 1
# majalah = {
#     'judul': 'argentina juara',
#     'penulis': 'angkara vito'
# }

# #cara 2
# majalah = dict(
#     judul='argentina juara',
#     penulis='angkara vito'
# )

# #nested dictionary
# Dict = { 
#         1: 'Aldi', 
#         2: 'ulbi', 
#         3: {'anggota1': 'aldi', 'anggota2': 'vito', 'anggota3': 'ridla'} 
# }
# print(Dict)

# #dictionary kosong
# nol = {}

# #menggunakan kurung siku
# kuliah = {
#     'nama': 'ulbi',
#     'proditop': 'sains data'
# }
# #panggil semua
# print(kuliah)
# #panggil spesifik
# print('nama univ:', kuliah['nama'])

# #menggunakan get
# majalah1 = dict(
#     judul="ARGENTINA JUARA",
#     penulis="Angkara", 
# )
# print('Judul:', majalah.get('judul'))
# print('Judul:', majalah.get('penulis'))

# #menggunakan get pada nested dictionary
# Dict = { 
#     1: 'Aldi', 
#     2: 'ulbi', 
#     3: {'anggota1': 'aldi', 'anggota2': 'vito', 'anggota3': 'ridla'} 
# }
# print('Mengakses nested:', Dict.get(3).get('anggota3'))

# #perulangan
# buku = {
#     'judul': 'hitler lahir di garut',
#     'penulis': 'Atep'
# }

# for key in buku:
#     print(key, ':', buku[key])

#mengubah nilai
presiden = {
    'nama': 'jokowi',
    'thnjabat': '3 periode',
    'asal': 'Indonesia'
}
print('jawbatan awal:', presiden.get('thnjabat'))
presiden['thnjabat'] = '2periode'
print('Setelah diubah:', presiden.get('thnjabat'))

siswa = {
    'nama': 'Muhammad Ibnu',
    'umur': '21thn',
    'asal': 'Jabar'
}
siswa['hobi'] = 'Memancing'
print(siswa)

#menghapus item
#del
siswa = {
    'nama': 'Muhammad Ibnu',
    'umur': '21thn',
    'asal': 'Jabar'
}
del siswa['nama']
print(siswa)
#pop
siswa = {
    'nama': 'Muhammad Ibnu',
    'umur': '21thn',
    'asal': 'Jabar'
}
print(siswa.pop('nama'))
print(siswa)

# #LAPRAK 
# #menghapus semua item dari dictionary
# worlcup= dict(
#    nama_tim = ("Argentina","Portugal","Prancis","Maroko","Kroasia"),
#    nama_pemain = ("Messi","Mbappe","Modric","Hakimi","Ramos"),
#    pemain_terbaik = "Messi",
# )
# dict.clear(worlcup)
# print(worlcup) 

# #menyalin dictionary  dengan metode copy()
# dictionary1 = {
#     "partai": "Banteng Merah",
#     "slogan" : "3 priode atau tidak sama sekali !!! ",
# }
# dict2 = dictionary1.copy() 
# print (dict2) 

 
# #mengeluarkan item dictionary menjadi list
# pemain = {
#     'nama' : "Ronaldo",
#     'hobi' : "duduk di bangku cadangan",
#     'pencapaian world cup 22' : "pulang duluan"
# }
# print(pemain.items()) 

# #mengembalikan daftar dari pasangan tuple
# Indonesia = dict (
#     Squad = ("firman utina","atep","markus","gonzalez"),
#     jumlah = "23 orang",
#     pelatih = "djajang nurjaman",
# )
# Indonesia.popitem()
# print(Indonesia) 

# #menampilkan semua key 
# Argentina = dict (
#     pemainterbaik = "Acuna a.k.a deni",
#     Prestasi = "juara world cup",
# )
# print(Argentina.keys())

# #menampilkan semua value pada dictionary
# Orang_Sakti = dict(
#     nama = " Gus Samsudin",
#     umur = "1001 tahun",
#     quotes = "hooh tenanan",
# )
# print(Orang_Sakti.values())

# #mengupdate value dari dictionary
# Riza = {
#     'nama': "vini",
#     'umur': "19 tahun",
#     'asal': "garut",
# }
# Riza.update({'nama':"Jihan"})
# print(Riza)

# #menghitung panjang total dictionary
# person = dict(
#     nama = "aldi daim",
#     umur = "20 tahun",
#     kesibukan = "mengurus web sains data",
#     asal = "cimahi",
#     suka = "ngopi",
# )
# print(len(person))


# #merepresentasikan string dari dictionary
# Messi = dict(
#     pencapaian2022= "juara world cup",
#     balon_dor= "7 ballon d'or",
#     klub = "PSG"
# )
# print(str(Messi))

# #mengembalikan tipe variabel,contohnya "type"({})
# # akan di kembalikan menjadi tipe data dictionary
# Prodi = {
#     'nama':"Sains Data",
#     'jumlah mahasiswa' :"26 orang",
#     'nama HIMA':"HIMASTA"
# }
# print(type(Prodi))

# #SOAL 
# #1A
# Mahasiswa = {
#     'nama' : 'aldi',
#     'umur' : '20 tahun',
#     'tinggi' : '170.5',
#     'hobi' : 'olahraga'
# }
# print(Mahasiswa)

# #1B
# Siswa = dict(
#     nama = 'aldi',
#     umur = '20 tahun',
#     tinggi = 170.5,
#     hobi = 'olahraga'
# )
# print(Siswa)

# #2
# Kampus = {
#     'universitas': 'ULBI',
#     'fakultas': 'FLTB',
#     'jurusan': {'jurusan1': 'sainsdata', 'jurusan2': 'bisnisdigital', 
#     'jurusan3': 'manlog','jurusan4':'mantra','jurusan5':'manrek'}
# }
# print("variabel nested = ",Kampus.get('jurusan'))

# #3
# dict2= dict (
#     nama = "aldi",
#     umur = "20 tahun",
#     tinggi = 170.5 ,
#     hobi = "olahraga"
# )
# print(dict2.get('nama'))

# #4
# pemain_bola = dict (
#     nama = 'Ronaldo',
#     klub_lama='Manchester United',
#     klub_baru = 'Al-nassr',
#     umur = '35 tahun'
# )
# print('klub asal:', pemain_bola['klub_lama'])

# #5
# dict3 = {
#     'Nama': 'Zara', 
#     'Umur': 16, 
#     'Kelas': '11 SMA'}
# dict3['Umur']= 17
# dict3['Kelas']= '12 SMA'
# print(dict3)

# #6
# dict4 = {
#     'Nama': 'Zara', 
#     'Umur': 17, 
#     'Kelas': '12 SMA',
#     'Asal': 'Sukabumi'}
# print(dict4)

# #7
# avengers = {
#     'Squad' : {'Iron Man','Spiderman','Hulk','Captain Marvel','Thor','Captain America'},
#     'Production Company' : 'Marvel Studio',
#     'Directors' : {'Anthony Russo','Joe Russo'},
# }
# avengers.popitem()
# print(avengers)

# #8
# Pawang_hujan = dict(
#     nama = " Mba Rara",
#     umur = "888 tahun",
#     hobi = "memberhentikan hujan",
# )
# print(Pawang_hujan.keys())

# #9
# Pawang_hujan = dict(
#     nama = " Mba Rara",
#     umur = "888 tahun",
#     hobi = "memberhentikan hujan",
# )
# print(Pawang_hujan.values())

# #10
# Presiden ={
#     'Nama'          :'Jokowi',
#     'Umur'          :'61 tahun',
#     'tahun menjabat':'10 Tahun',
#     'Asal'          :'Solo'
# }
# print(Presiden.items())

# #11
# pemain = {
#   "nama"    : "Neymar",
#   "umur"    : '31 tahun',
#   "tinggi"  : 177.6,
#   "klub"    : 'PSG',
#   'negara'  : 'Brasil'
# }
# print(len(pemain))

# #12
# mugiwara = {
#     'captain' : 'Luffy',
#     'kapal'   : 'sunny go',
#     'kru'     : ('sanji','zoro','nami','jinbe','brook','chopper','usoop','robin')
# }
# print(str(mugiwara))