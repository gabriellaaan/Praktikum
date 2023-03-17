class StringList184220028 (list):
    def __init__(self):
        self.data = []
    def __repr__(self):
        return str(self.data)
    def append(self, objek):
        if not isinstance(objek, str):
            raise TypeError('Objek harus bertipe string')
        self.data.append(objek)
    def insert(self, indeks, objek):
        if indeks >= len(self.data) or \
        indeks < -len(self.data):
            raise IndexError('Indeks di luar rentang')
        if not isinstance(objek, str):
            raise TypeError('Objek harus bertipe string')
        self.data.insert(indeks, objek)

slist = StringList184220028()
slist.append('Python')
slist.append('Ruby')
slist.append('PHP')
print(slist)
slist.insert(2, 'Perl')
print(slist)
slist.insert(-3, 'Java')
print(slist)
#slist.append(99)
#slist.insert (2, 100)
slist.insert(-6, 'JavaScript')