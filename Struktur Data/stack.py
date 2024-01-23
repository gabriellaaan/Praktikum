# stk = [1,2,3,4,5]
# print (stk)

# #memasukkan data baru 
# stk.append(11)
# print("data masuk", 11)
# print("data sekarang", stk)

# stk.append(15)
# print("data masuk", 15)
# print("data sekarang", stk)

# #mengeluarkan data
# datakeluar = stk.pop()
# print("data yang keluar adalah :", datakeluar)
# print("data terakhir adalah:", stk)

# class stack :
#     def __init__ (self) :
#             self.items = []
#     def isEmpty (self) :
#             return self.items == []
#     def push (self, item) :
#             self.items.append (item)
#     def pop (self) :
#             return self.items.pop()
#     def peek (self) :
#             return self.items [len(self.items)-1]
#     def size (self) :
#             return len(self.items)

# s = stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# #Jumlah Buku Pada 10 Januari 2022
# buku = [1,2,3,4,5,6,7]
# print("Jumlah Buku Awal:", buku) 

# #Penambahan Buku Pada 10 April 2022
# buku.append(8)
# print("Penambahan Buku", 8)
# print("Jumlah Buku :", buku)
# buku.append(9)
# print("Penambahan Buku", 9)
# print("Jumlah Buku :", buku)

# #Pengambilan Buku oleh Pelanggan Pada 11 April 2022
# buku.pop()
# print("Pengambilan Buku oleh Pelanggan", buku)
# print("Jumlah Buku :", buku)


#1 - 3
s = [90,100,250,600,700,1000,2000]
# 1
s.append(5000)
print("data setelah ditambahkan : ", s)
#2
s.append(10000)
print("data setelah ditambahkan :", s)
#3
s.pop()
print('data sekarang :', s)

#4 - 6
s1 = [11,44,56,98,143,234,167]
#4
s1.pop()
print('data :', s1)
#5
s1.append(475)
print("data sekarang :", s1)
#6
s1.pop()
print('data sekarang :', s1)
s1.pop()
print("data akhir :", s1)
 #7
# soal praktikum
#Jumlah Buku Pada 10 Januari 2022
buku = [1,2,3,4,5,6,7]
print ("Jumlah Buku Awal:" ,buku)

#Penambahan Buku pada 10 April 2022
buku.append(8)
print("Penambahan Buku",8)
print("Jumlah Buku : ",buku)

#Penambahan Buku Pada 10 April 2022
buku.append(9)
print("Penambahan Buku",9)
print("Jumlah Buku : ",buku)

#Pengambilan Buku oleh Pelanggan Pada 11 April 2022
buku.pop()
print("Pengambilan Buku oleh Pelanggan",buku)
print("Jumlah Buku : ",buku)
#Pengambilan Buku yang terakhir ditumpuk menjadi Buku yang pertama kali diambil oleh Pembeli

# 8 
sepedamotor = [1,2,3]
print ("Jumlah Sepeda Motor :" ,sepedamotor)

#Penambahan Sepeda Motor Baru yang akan disimpan oleh teman mas wahyu
sepedamotor.append(4)
print("Penambahan Sepeda motor menjadi",4)
print("Jumlah Sepeda Motor : ",sepedamotor)

#Pengambilan Sepeda Motor ole teman mas wahyu
sepedamotor.pop()
print("Pengambilan Sepeda Motor",sepedamotor)
print("Jumlah Sepeda Motor : ",sepedamotor)

#Pengambilan Sepeda Motor oleh adik mas wahyu
sepedamotor.pop()
print("Pengambilan Sepeda Motor ",sepedamotor)
print("Jumlah Sepeda Motor : ",sepedamotor)