
def merge_sort(arr):
    if len(arr) > 1:
        # array dibagi 2
        tengah = len(arr) // 2
        left_arr = arr[:tengah]
        right_arr = arr[tengah:]
        # pemecahan
        merge_sort(left_arr)
        merge_sort(right_arr)
        # penggabungan
        i,j,k = 0,0,0 # indeks left_arr, right_arr dan hasil akhir
        print("Sebelum Merge:", arr)
        print("Potongan sebelum Merge:", left_arr, ":", right_arr)
        while i < len(left_arr) or j < len(right_arr):
            if i == len(left_arr): # elemen di potongan kiri habis
                arr[k] = right_arr[j]
                j = j + 1
            elif j == len(right_arr): # elemen di potongan kanan habis
                arr[k] = left_arr[i]
                i = i + 1
            elif left_arr[i] <= right_arr[j]: # nilai elemen di potongan kiri lebih kecil
                arr[k] = left_arr[i]
                i = i + 1
            else: # nilai elemen di potongan kanan lebih besar
                arr[k] = right_arr[j]
                j = j + 1
            k = k + 1
        print("Setelah Merge:", arr)
        print() # enter
 
angka = [2, 6, 7, 4, 3, 5, 1]
print("Sebelum Sort:", angka)
print()
merge_sort(angka)

