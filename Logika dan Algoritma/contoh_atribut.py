class ClubBolaEl:
    counter = 0
    def __init__(self, p, l):
        ClubBolaEl.counter += 1
        self.pemain = p
        self.club = l
    def NamaPemain(self, p):
        self.pemain = p
    def NamaClub(self, l):
        self.club = l

 #objek
obj1 = ClubBolaEl ("Mohamed Salah", "Cirebon FC")
obj2 = ClubBolaEl ("Christian Ronaldo", "Bekasi FC" )
obj3 = ClubBolaEl ("Lionel Messi", "Citayam FC")
obj4 = ClubBolaEl ("Mbappe", "Riyadh FC")
obj5 = ClubBolaEl ("Budi Soedarsono", "Buah Batu FC")
print(ClubBolaEl.counter)
print(obj1.counter)
print(obj2.counter)
print(obj3.counter)
print(obj1.pemain,obj1.club)
print(obj2.pemain,"berasal dari",obj2.club,"kalah melawan", 
    obj5.pemain,"dari",obj5.club)
