def quick_sort(arr):
    # Jika panjang array <= 1, array sudah terurut
    if len(arr) <= 1:
        return arr
    
    # Pilih elemen terakhir sebagai pivot
    pivot = arr[-1]
    
    # Pisahkan elemen lebih kecil dan lebih besar dari pivot
    smaller = [x for x in arr[:-1] if x <= pivot]  # Semua elemen <= pivot
    larger = [x for x in arr[:-1] if x > pivot]   # Semua elemen > pivot

    # Gabungkan hasil rekursif
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

# Contoh penggunaan
data = [10, 7, 8, 1, 5, 9, 2]
print("Sebelum diurutkan:", data)
sorted_data = quick_sort(data)
print("Setelah diurutkan:", sorted_data)
