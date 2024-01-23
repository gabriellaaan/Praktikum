#membuat list terlebih dahulu
list = ["tata", "ecil", "ale", "el"]

#fungsi built-in len untuk memberikan total panjang isi list
print(len(list))

#fungsi built-in max untuk mencari item bernilai maksimal
print(max(list))

#fungsi built-in min untuk mencari item bernilai minimum
print(min(list))

#method built-in append untuk menambahkan item dalam list
list.append("ela")
print(list)

#method built-in count untuk mengetahui kuantitas item
print(list.count("tata"))

#method built-in extend untuk menambah item pada list
print(list.index("ale"))
print(list)

print()

#method built-in insert untuk menyisipkan item pada list
list.insert(1,"coco")
print(list)

#method built-in pop untuk menghapus item terakhir atau tertentu pada list
print(list.pop())
print(list)
print(list.pop(2))
print(list)

#method built-in remove untuk menghapus item tertentu pada list
list.remove("tata")
print(list)

#method built-in reverse untuk membuat posisi item pada list secara terbalik
list.reverse()
print(list)
