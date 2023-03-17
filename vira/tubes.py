def fungsiburger():
    global totalburg
    global bayar
    global extra
    global pilihan
    
print("------WELCOME TO BURGER QUEEN------")
A = str(input("Masukkan Nama Pembeli : "))
print("Nama Pembeli : " + A)

print("-------MENU--------")
print("1. Burger ")
print("2. Snack ")
print("3. Minuman")
A = int(input("Masukkan Pilihan (please type only the number) : "))
if (A == 1) :
    print("---BURGER---")
    print("1. Burger Ayam Rp. 15000")
    print("2. Burger Sapi Rp. 20000")
    B = int(input("Masukkan Pilihan (please type only the number): "))
    if (B == 1) :
        BB = int(input("Masukkan Jumlah Porsi : "))
        for x in range (BB):
            bucket = 15000
            print(f"Burger ke-{x + 1} : ")
            print("--Extra Cheese +3000 --")
            print("1. Yes i want extra cheese !")
            print("2. No im fine :)")
            C = int(input("Masukkan Pilihan (please type only the number) : "))
            if (C == 1) :
                bucket2 = bucket + 3000
            elif (C==2) :
                bucket3 = bucket
                print (BB, "Porsi Burger = Rp." + str(bucket2+bucket3))   
                


                

            


