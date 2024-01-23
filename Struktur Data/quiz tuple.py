# tuple_genshin = ('Hutao', 'Kazuha', 'Xiao', 'Ayato')
# print(tuple_genshin[0])         #1
# print(tuple_genshin[:2])        #2
# print(tuple_genshin[-2:])       #3
# print(tuple_genshin[:2])        #4
# print(tuple_genshin[1:3])       #5

# t1 = (12,3,10,50,66,71,8,11,9,23)
# print(t1[0:])         #6
# print(t1[0])          #7
# print(t1[-4:-1])      #8
# print(t1[::-1])       #9
# print(t1[1:])         #10

# tuple_nama_pemain=('ronaldo','messi','neymar','suarez','halland','rooney','puyol','maradona','pele','van persie')
# print(tuple_nama_pemain[0])     #11
# print(tuple_nama_pemain[1])     #12
# print(tuple_nama_pemain[8])     #13
# print(tuple_nama_pemain[3])     #14
# print(tuple_nama_pemain[7])     #15
# print(tuple_nama_pemain[-8])    #16
# print(tuple_nama_pemain[-5])    #17
# print(tuple_nama_pemain[-6])    #18
# print(tuple_nama_pemain[6])     #19
# print(tuple_nama_pemain[-1])    #20

# tuple_honkai = ( 'kiana', 'durandal', 'sushang', 'elysia')
# print(tuple_honkai[3:])     #21
# print(tuple_honkai[::-1])   #22
# print(tuple_honkai[2:])     #23
# print(tuple_honkai[:1])     #24
# print(tuple_honkai[:2])     #25

# Tup1=(19,28,33)
# Tup2=('kamu','aku','dia')
# Tup3=('kita','mereka','kalian')
# Tup4=(7,16,10,20,4)
# print(Tup1+Tup2)                #26
# print(Tup2+Tup4)                #27
# print(Tup3+Tup4)                #28
# print(Tup1+Tup3)                #29
# print(Tup1+Tup4)                #30
# print(Tup3+Tup2)                #31
# print(Tup1+Tup4+Tup3)           #32
# print(Tup2+Tup3+Tup1)           #33
# print(Tup1+Tup2+Tup3+Tup4)      #34
# print(Tup4+Tup3+Tup2+Tup1)      #35     
# p = Tup1,Tup2                   #36
# print(p)
# q = Tup1,Tup3                   #37
# print(q)
# r = Tup2,Tup3,Tup4              #38
# print(r)
# s = Tup1,Tup2,Tup3              #39
# print(s)
# t = Tup4,Tup3,Tup2,Tup1         #40
# print(t)

# tuple9=(7,8,1,4,5,8,7,2,1,9,0,1,2,7,2,9,3,6,7,8,9)
# print(tuple9.count(7))      #41
# print(tuple9.count(2))      #42
# print(tuple9.count(1))      #43
# print(tuple9.count(8))      #44
# print(tuple9.count(0))      #45

# t2= (4,3,12,10,26,17,20,2,33,51,67)
# print(t2[0:])               #46
# print(t2[:5])               #47
# print(t2[10:])              #48
# print(t2[6:])               #49
# print(t2[-6:])              #50

# tuple1= 'ronaldo','the real','goat','mempunyai',5,'piala ucl'
# print(tuple1.index('goat'))         #51
# print(tuple1.index('ronaldo'))      #52
# print(tuple1)                       #53
# print(tuple1.index('piala ucl'))    #54
# print(tuple1.index(5))              #55

# tuple3= (22,19,12,3,13,2,20)
# print(len(tuple3))      #56
# print(max(tuple3))      #57
# print(min(tuple3))      #58

# tup01 = (30,41,20,12,3)
# print(len(tup01))           #59
# print(max(tup01))           #60
# print(min(tup01))           #61
# tpx = tuple('Thiodas')      #62
# print(tpx)
# tpy = tuple('Bluelock')     #63
# print(tpy)
# tpz = tuple('EVANGELION')   #64
# print(tpz)
# tpv = tuple('GABRIELLA')    #65
# print(tpv)

tup_odd = 1,3,5,7,9          
tup_odd1 = 11,13,15,17,19    
# print(tup_odd + tup_odd1)                   #66
# print(2 in tup_odd, 2 in tup_odd1)          #67
         
# tup_odd2 = tup_odd,tup_odd1
# print(tup_odd2)                             #68
# print(tup_odd*3)                            #69
# print(19 in tup_odd)                        #70
# print(19 in tup_odd1)        
# print(tup_odd1*5)                           #71
# print(tup_odd2*5)                           #72

# print(tup_odd +tup_odd1 + tup_odd2)                                         #73
# print('genap' in tup_odd, 'genap' in tup_odd1, 'genap' in tup_odd2)         #74  
   
# for i in tup_odd:        
#     print(i, end='')                        #75

# for j in tup_odd2:
#     print(j, end='')                      #76

# print(tup_odd[1:5])                       #77
# print(tup_odd[-5:-1])                     #78
# print(tup_odd1[1:5])                      #79
# print(tup_odd1[-5:-1])                    #80

# gizi = ('Nasi', 'Ayam', 'Sayuran')              #81
# karbohidrat, protein, serat = gizi
# print('karbohidrat :', karbohidrat)
# print('protein :', protein)
# print('serat :', serat) 

# data_hobi = ('ren', 'membaca webtoon')          #82
# nama,hobi = data_hobi
# print('nama :', nama)
# print('hobi :', hobi)

# data_mahasiswa = ('phil', 20, 'psikologi')      #83
# namae, umur, prodi = data_mahasiswa
# print('nama :', namae)
# print('umur :', umur)
# print('prodi :', prodi)

# BG = ('SEVENTEEN', 2015, 'South Korea')         #84
# sebutan, debut, asal=BG
# print('grup :', sebutan)
# print('debut :', debut)
# print('asal :', asal)

# data_perusahaan = ('POS', 'Logistik', 'BUMN')   #85
# perusahaan, bidang, status = data_perusahaan
# print('perusahaan :', perusahaan)
# print('bidang :', bidang)
# print('status :', status)

# q1 = [12, 'Maysa', 'Cintay', 'Fahriza']                             #86
# q11 = tuple([12, 'Maysa', 'Cintay', 'Fahriza'])
# print(q11) 

# q2 = ['Raiden', 'Aponia', 'Mobius', 'Kaslana', 'Keqing']            #87
# q22 = tuple(['Raiden', 'Aponia', 'Mobius', 'Kaslana', 'Keqing'])
# print(q22) 

# q3 = [34,78,99,32,8,7, 'angka']                                     #88
# q33 = tuple([34,78,99,32,8,7, 'angka'])
# print(q33) 

# q4 = ['Saya', 'Ingin', 'Menjadi', 'Anime']                          #89
# q44 = tuple(['Saya', 'Ingin', 'Menjadi', 'Anime'])
# print(q44) 

# q5 = ['Kazuha', 'Pacar', 'Salwa', 'HeHe']                           #90
# q55 = tuple(['Kazuha', 'Pacar', 'Salwa', 'HeHe'])
# print(q55) 

# D1 = {'Sains', 'data', 'Best', 'prodi'}                     #91
# D11 = tuple(D1)
# print(D11) 

# D2 = {1,3,5,7,9,10,8}                                       #92
# D22 = tuple(D2)
# print(D22)

# D3 = {2023, 'Bisa', 'Lebih', 'Baik'}                        #93
# D33 = tuple(D3)
# print(D33)

# D4 = {'Saya','Keren', 'Dan', 'Hebat'}                       #94
# D44 = tuple(D4)
# print(D44) 

# D5 = {'Matkul', 'StrukturData', 'Sangat', 'Menyenangkan'}   #95
# D55 = tuple(D5)
# print(D55) 

Tup4=(7,16,10,20,4)
print(Tup4.index(10))       #96
print(len(Tup4))            #97
print(max(Tup4))            #98
print(min(Tup4))            #99
for g in Tup4 :
 print(g, end = '')         #100