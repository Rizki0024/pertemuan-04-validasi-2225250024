# Menampilkan judul program
print("\n=== Validasi Tipe dan Pengecekan Ketuntasan Soal ===")

# Mengambil input dari pengguna
teks = input("Jumlah soal benar dari 20: ").strip()

# Validasi tipe data menggunakan try-except
try:
    benar = int(teks)
except ValueError:
    print("\n=== Hasil Pengecekan ===")
    print("Masukan ditolak: jumlah harus berupa bilangan bulat.")
else:
    # Validasi rentang nilai
    if benar < 0 or benar > 20:
        print("\n=== Hasil Pengecekan ===")
        print("Masukan ditolak: jumlah harus berada pada rentang 0 sampai 20.")
    else:
        persen = (benar / 20) * 100
        print("\n=== Hasil Pengecekan ===")
        print(f"Persentase = {persen:.2f} persen")
        
        if persen >= 75:
            print("Status     = Tuntas")
        else:
            print("Status     = Belum tuntas")