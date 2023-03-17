import time
masa_lalu = time.time()
print ('waktu yang telah berlalu sejak awal adalah :', masa_lalu)

import time
waktu = 1670982793.7977715
hasil = time.ctime(waktu)
print("waktu yang didapat saat ini adalah : ", hasil)

print ("BATAS".center(20,":"))

import time
waktu1 = time.sleep(15)
print ("website Prodi Sains Data Terbaik Puoll")

print()

import time
localtime = time.localtime(waktu)
print("waktu saat ini : ", localtime)

print ("BATAS". center(20,":"))

import time
waktu_pertama = time.localtime()
waktu_kedua = time.strftime("%m/%d/%Y, %H:%M:%S", waktu_pertama)
print(waktu_kedua)

print ("BATAS". center(20,":"))

import datetime
time = datetime.datetime.now()
print(time)

print()

import datetime
waktu = datetime.datetime(2022, 12, 14,9, 16, 35)
print (waktu.year)
print (waktu.month)
print (waktu.day)
print (waktu.hour)
print (waktu.minute)
print (waktu.second)

print ()

import datetime
waktu1 = datetime.datetime(2022, 12, 11, 21, 23, 40)
print(waktu1.strftime("%A,%d %b %Y, %I:%M:%S %p"))

print ()

import datetime
waktu_jadian = datetime.datetime(2022, 2, 14, 15, 30, 30)
waktu_putus = datetime.datetime(2022, 6, 27, 23, 59, 59)
jadi_mantan = (waktu_putus - waktu_jadian).days//30
waktu_pacaran = waktu_jadian - waktu_putus
print (jadi_mantan)
print (waktu_pacaran) 

print ()
 
import datetime
mulai = datetime.datetime(2020, 12, 15, 21, 30, 0)
akhir = mulai + datetime.timedelta(days= 30, hours= 5)
print (akhir.strftime("%d %B %Y, pukul %I:%M:%S"))

print ()

import calendar
yy = 2004
mm = 9
print (calendar.month(yy,mm))

print()

import calendar
year = 2023
print (calendar.calendar(year))
