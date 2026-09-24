# Menampilkan judul program
print("\n=== Klasifikasi Predikat Nilai ===")

# Mengambil input dari pengguna
nilai = float(input("Nilai akhir (0-100): "))

# Mengecek predikat berdasarkan rentang nilai
if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"

# Menampilkan hasil
print("\n=== Hasil Pengecekan ===")
print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")