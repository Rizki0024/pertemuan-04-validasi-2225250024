# Menampilkan judul program
print("\n=== Klasifikasi Kategori Bilangan ===")

# Mengambil input dari pengguna
x = int(input("Masukkan bilangan bulat: "))

# Mengecek kategori bilangan
if x < 0:
    kategori = "Bilangan negatif"
elif x == 0:
    kategori = "Nol"
elif x % 2 == 0:
    kategori = "Bilangan positif genap"
else:
    kategori = "Bilangan positif ganjil"

# Menampilkan hasil
print("\n=== Hasil Pengecekan ===")
print(f"Kategori: {kategori}")