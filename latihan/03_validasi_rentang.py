# Menampilkan judul program
print("\n=== Validasi dan Klasifikasi Jenis Sudut ===")

# Mengambil input dari pengguna
sudut = float(input("Besar sudut dalam derajat: "))

# Validasi rentang dan klasifikasi jenis sudut
if sudut <= 0 or sudut >= 180:
    print("\n=== Hasil Pengecekan ===")
    print("Masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
elif sudut < 90:
    print("\n=== Hasil Pengecekan ===")
    print("Jenis sudut: Sudut lancip")
elif sudut == 90:
    print("\n=== Hasil Pengecekan ===")
    print("Jenis sudut: Sudut siku-siku")
else:
    print("\n=== Hasil Pengecekan ===")
    print("Jenis sudut: Sudut tumpul")