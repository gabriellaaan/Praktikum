# tuple1 = ('SEVENETEEN','NCT', True, 2022,2023) 
# tuple2 = 1,3,5,7,9 #tuple tanpa tanda kurung
# tuple3 = () #tuple kosong
# tuple4 = ('naruto',) #tuple 1 elemen


# tuple_HYBE = ('EN-','TXT','LE SSERAFIM','NEW JEANS') 
# print(type(tuple_HYBE))

# tuple_mix ='benda','sifat', 13, 29
# print(tuple_mix, type(tuple_mix))

# tuple_00 = tuple([True,'Tokyo',2468,'Seoul']) 
# print(tuple_00, type(tuple_00))

# #mengakses tuple (cara standar/indexing)
# tuple_anemo_boy = ('kazuha', 'xiao', 'xavier') 
# print(tuple_anemo_boy[1]) 
# print(tuple_anemo_boy[0]) 
# print(tuple_anemo_boy[-1])

# #mengakses tuple (sequence unpacking)
# mahasiswa = 'Riza', 'Zimbabwe', 'sains data', 22
# nama, asal, prodi, angkatan = mahasiswa
# print('Nama:', nama) 
# print('Asal:', asal) 
# print('Prodi:', prodi) 
# print('Angkatan:', angkatan)

# #nested tuple
# tup1 = (12, 34.56) 
# tup2 = ('abc', 'xyz') 
# tup3 = tup1,tup2
# print(tup3)

# #mengakses nilai elemen tuple pada tipe data tuple (nested tuple)
# t=((3,5,7),(9,5,1),(8,5,2)) 
# print(t[0][1]) 
# print(t[1][-1]) 
# print(t[-2][-3])

# #modifikasi tuple (megubah/meng-update)
# tuple5 = ('USA','UK','ROK','PRC') 
# tuple5[1] = ('KSA') 
# print(tuple5)

# #menghapus tuple secara keseluruhan
# tuple6 = 'Japan',1945,'Indonesia'
# del tuple6
# print(tuple6)

#indexing of tuple
t = (11,13,15,17)
t[2]

# #slicing of tuple
# t1=(1,3,5,9,7,11,13,15,17) 
# print(t1[1:]) #1
# print(t1[:7]) #2
# print(t1[1:5]) #3
# print(t1[::-1]) #4
# print(t1[-6:-1]) #5

#Built-In Method
#count
t2 = (1,3,2,3,4,3,5,3,6,3) 
print(t2.count(3)) 
#index
t3='sapi','ayam','ikan','kambing','udang'
print(t3.index('ikan'))

#Built-In Function
#len()
tup4= 2,4,6,8,10,11,12
print(len(tup4)) 
#max()
tup4= 2,4,6,8,10,11,12
print(max(tup4)) 
#min()
tup4= 2,4,6,8,10,11,12
print(min(tup4)) 
#tuple()
tup5 = tuple('Luxemburg') 
print(tup5, type(tup5))

# tuple = (1,2,3)
# print(len(tuple))
# print(tuple + (4,5,6))
# print(tuple*2)
# print(3 in tuple)
# for x in tuple:
#     print(x, end = '')