# Menampilkan judul program
print("\n=== Klasifikasi Segitiga Berdasarkan Sudut ===")

# Mengambil input dari pengguna
a = float(input("Sudut A: "))
b = float(input("Sudut B: "))
c = float(input("Sudut C: "))

# Validasi nilai sudut positif dan total sudut = 180
if a <= 0 or b <= 0 or c <= 0:
    print("\n=== Hasil Pengecekan ===")
    print("Masukan ditolak: setiap sudut harus lebih dari 0 derajat.")
elif abs(a + b + c - 180) > 1e-9:
    print("\n=== Hasil Pengecekan ===")
    print("Masukan ditolak: jumlah ketiga sudut harus 180 derajat.")
else:
    terbesar = max(a, b, c)
    print("\n=== Hasil Pengecekan ===")
    if terbesar > 90:
        print("Jenis Segitiga: Segitiga tumpul")
    elif terbesar == 90:
        print("Jenis Segitiga: Segitiga siku-siku")
    else:
        print("Jenis Segitiga: Segitiga lancip")