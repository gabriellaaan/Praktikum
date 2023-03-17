# from collections import deque
# antrian = deque([1,2,3,4,5])
# antrian.append(6)
# antrian.popleft()
# print(antrian)

# from collections import deque #import module
# antrian = deque([1,2,3,4,5])
# print('data antrian sekarang :', antrian)

# #menambahkan data antrian
# antrian.append(6)
# print('data antrian masuk : 6')
# print('data antrian : ', antrian)

# #mengurangi antrian
# keluar = antrian.popleft()
# print('data keluar : ', keluar)
# print('data antrian sekarang : ', antrian)

# from collections import deque
# #Jumlah antrian siang pukul 15.00 WIB
# antrian = deque([5,6,7,8,9])

# print("Jumlah antrian : ", antrian)

# #Antrian bertambah/ pelangan baru pada pukul 15.10 WIB
# antrian.append(10)
# print("Pembeli ke-", 10)
# print("Jumlah antrian :", antrian)

# #Antrian bertambah/ pelangan baru pada pukul 15.15 WIB
# antrian.append(11)
# print("Pembeli ke-", 11)
# print("Jumlah antrian :", antrian)

# #Antrian berkurang pada pukul 15.15 WIB
# out = antrian.popleft()
# print("Pembeli yang keluar", out)
# print("Jumlah pembeli :", antrian)

# #Antrian berkurang pada pukul 15.16 WIB
# out = antrian.popleft()
# print("Pembeli yang keluar", out)
# print("Jumlah pembeli :", antrian)


# # B Queue

from collections import deque # import module
antrian = deque([10,11,12,13,14])
print('data antrian sekarang : ', antrian)
 
#menambahakan data antrian
antrian.append(15)
print('data antrian masuk : 15')
print('data antrian : ', antrian)
 
#mengurangi antrian
keluar = antrian.popleft()
print('data keluar : ', keluar)
print('data antrian sekarang : ', antrian)
keluar = antrian.popleft()
print('data keluar : ', keluar)
print('data antrian sekarang : ', antrian)

antrian.append(16)
print('data antrian masuk : 16')
print('data antrian sekarang :', antrian)

from collections import deque
#Jumlah Antrian Pagi Jam 10.00 WIB
antrian = deque([1,2,3,4,5])

print("Jumlah Antrian : ",antrian)

#Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.20 WIB
antrian.append(6)
print("Nasabah ke ",6)
print("Jumlah Antrian :",antrian)

#Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.30 WIB
antrian.append(7)
print("Nasabah ke ",7)
print("Jumlah Antrian :",antrian)
#Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.30 WIB
antrian.append(8)
print("Nasabah ke ",8)
print("Jumlah Antrian :",antrian)

#Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.35 WIB
out = antrian.popleft()
print("Nasabah yang keluar",out)
print("Jumlah Nasabah Sekarang :",antrian)

#Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.40 WIB
out = antrian.popleft()
print("Nasabah yang keluar",out)
print("Jumlah Nasabah Sekarang :",antrian)