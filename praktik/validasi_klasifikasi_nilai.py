# Menampilkan judul program
print("\n=== Validasi dan Klasifikasi Nilai Akhir ===")

# Mengambil input dari pengguna dan membersihkan spasi di awal/akhir
teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

# Validasi Tipe: Memastikan input dapat dikonversi menjadi float
try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("\n=== Hasil Pengecekan ===")
    print("Masukan ditolak: seluruh data harus berupa angka.")
else:
    # Validasi Rentang: Memastikan input berada dalam interval 0 - 100
    if not (0 <= ujian <= 100):
        print("\n=== Hasil Pengecekan ===")
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")
    elif not (0 <= tugas <= 100):
        print("\n=== Hasil Pengecekan ===")
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")
    elif not (0 <= hadir <= 100):
        print("\n=== Hasil Pengecekan ===")
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")
    else:
        # Menghitung nilai akhir dengan bobot 60% Ujian dan 40% Tugas
        akhir = 0.6 * ujian + 0.4 * tugas
        
        print("\n=== Hasil Pengecekan ===")
        print(f"Nilai akhir  : {akhir:.2f}")

        # Pengecekan syarat kehadiran minimal 80%
        if hadir < 80:
            print("Status       : Tidak memenuhi syarat kehadiran")
        else:
            # Klasifikasi predikat berdasarkan rantai if-elif-else
            if akhir >= 85:
                predikat = "A"
            elif akhir >= 70:
                predikat = "B"
            elif akhir >= 60:
                predikat = "C"
            elif akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"

            # Penentuan status kelulusan berdasarkan predikat
            if predikat in ("A", "B", "C"):
                status = "Lulus"
            else:
                status = "Belum lulus"

            print(f"Predikat     : {predikat}")
            print(f"Status       : {status}")