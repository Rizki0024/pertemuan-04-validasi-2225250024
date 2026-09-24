# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

## Identitas

**Nama:** Rizki Ramadan  
**NIM:** 2225250024  
**Kelas:** 3F  

## Tujuan

Pada pertemuan ini saya mempelajari penggunaan seleksi multi-kondisi menggunakan rantai `if-elif-else` serta penerapan validasi masukan (tipe data, rentang nilai, dan domain). Saya juga mempelajari penggunaan struktur `try-except ValueError` untuk menangani kesalahan konversi data agar program tidak berhenti secara mendadak.

## Cara Menjalankan Program

Program dijalankan menggunakan Python melalui terminal di Visual Studio Code.

### Menjalankan Program Latihan

    python latihan/01_predikat_nilai.py
    python latihan/02_kategori_bilangan.py
    python latihan/03_validasi_rentang.py
    python latihan/04_validasi_tipe.py
    python latihan/05_klasifikasi_segitiga_sudut.py

### Menjalankan Tugas Praktik

    python praktik/validasi_klasifikasi_nilai.py

## Algoritma Program Praktik

### Validasi dan Klasifikasi Nilai Akhir

1. Membaca tiga masukan teks dari pengguna (nilai ujian, nilai tugas, dan kehadiran) serta membersihkan spasi awal/akhir menggunakan `.strip()`.

2. Memvalidasi tipe data masukan menggunakan `try-except ValueError` untuk memastikan seluruh masukan dapat dikonversi menjadi angka (`float`).

3. Memvalidasi rentang masukan menggunakan rantai `if-elif-else` untuk memastikan nilai ujian, tugas, dan kehadiran berada pada rentang 0 sampai 100.

4. Menghitung nilai akhir dengan rumus:

   Nilai Akhir = (0.6 × Ujian) + (0.4 × Tugas)

5. Memeriksa persentase kehadiran:
   - Jika kehadiran kurang dari 80%, tampilkan status "Tidak memenuhi syarat kehadiran".
   - Jika kehadiran minimal 80%, tentukan predikat berdasarkan nilai akhir:
     - 85 ≤ Nilai Akhir ≤ 100 → A
     - 70 ≤ Nilai Akhir < 85 → B
     - 60 ≤ Nilai Akhir < 70 → C
     - 50 ≤ Nilai Akhir < 60 → D
     - Nilai Akhir < 50 → E

6. Menentukan status kelulusan berdasarkan predikat:
   - Predikat A, B, dan C dinyatakan "Lulus".
   - Predikat D dan E dinyatakan "Belum lulus".

7. Menampilkan hasil perhitungan nilai akhir dengan format dua angka di belakang koma, predikat, dan status kelulusan.

## Tabel Keputusan (Praktik 1)

| **Kategori / Kondisi** |  **Syarat Logika**   |         **Contoh Input**         |                    **Output Diharapkan**                    |
|------------------------|----------------------|----------------------------------|-------------------------------------------------------------|
| Validasi Tipe          | Bukan angka          | `abc`                            | Masukan ditolak: seluruh data harus berupa angka.           |
| Validasi Rentang       | Ujian < 0 atau > 100 | `105`                            | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.  |
| Validasi Rentang       | Tugas < 0 atau > 100 | `-5`                             | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.  |
| Syarat Kehadiran       | Kehadiran < 80%      | Ujian: 90, Tugas: 90, Hadir: 75  | Nilai akhir: 90.00, Status: Tidak memenuhi syarat kehadiran |
| Predikat A             | Nilai Akhir >= 85    | Ujian: 90, Tugas: 80, Hadir: 95  | Nilai akhir: 86.00, Predikat: A, Status: Lulus              |
| Predikat B             | Nilai Akhir >= 70    | Ujian: 75, Tugas: 70, Hadir: 85  | Nilai akhir: 73.00, Predikat: B, Status: Lulus              |
| Predikat C             | Nilai Akhir >= 60    | Ujian: 60, Tugas: 60, Hadir: 80  | Nilai akhir: 60.00, Predikat: C, Status: Lulus              |
| Predikat D             | Nilai Akhir >= 50    | Ujian: 55, Tugas: 50, Hadir: 90  | Nilai akhir: 53.00, Predikat: D, Status: Belum lulus        |
| Predikat E             | Nilai Akhir < 50     | Ujian: 40, Tugas: 30, Hadir: 100 | Nilai akhir: 36.00, Predikat: E, Status: Belum lulus        |

## Hasil Pengujian

### 1. Praktik 1 - Validasi dan Klasifikasi Nilai Akhir (Utama)

|  **Input**  |                  **Hasil yang Diharapkan**                  |                      **Hasil Aktual**                       | **Status** |
|-------------|-------------------------------------------------------------|-------------------------------------------------------------|------------|
| 90, 80, 95  | Nilai akhir: 86.00, Predikat: A, Status: Lulus              | Nilai akhir: 86.00, Predikat: A, Status: Lulus              | Berhasil   |
| 75, 70, 85  | Nilai akhir: 73.00, Predikat: B, Status: Lulus              | Nilai akhir: 73.00, Predikat: B, Status: Lulus              | Berhasil   |
| 60, 60, 80  | Nilai akhir: 60.00, Predikat: C, Status: Lulus              | Nilai akhir: 60.00, Predikat: C, Status: Lulus              | Berhasil   |
| 55, 50, 90  | Nilai akhir: 53.00, Predikat: D, Status: Belum lulus        | Nilai akhir: 53.00, Predikat: D, Status: Belum lulus        | Berhasil   |
| 40, 30, 100 | Nilai akhir: 36.00, Predikat: E, Status: Belum lulus        | Nilai akhir: 36.00, Predikat: E, Status: Belum lulus        | Berhasil   |
| 90, 90, 75  | Nilai akhir: 90.00, Status: Tidak memenuhi syarat kehadiran | Nilai akhir: 90.00, Status: Tidak memenuhi syarat kehadiran | Berhasil   |
| 105, 80, 90 | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.  | Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.  | Berhasil   |
| 80, -5, 90  | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.  | Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.  | Berhasil   |
| 80, 80, abc | Masukan ditolak: seluruh data harus berupa angka.           | Masukan ditolak: seluruh data harus berupa angka.           | Berhasil   |

### 2. Pengujian Program Latihan (Latihan 01 - 05)

|          **File Latihan**          |  **Input**  |  **Hasil yang Diharapkan**   |       **Hasil Aktual**       | **Status** |
|------------------------------------|-------------|------------------------------|------------------------------|------------|
| `01_predikat_nilai.py`             | 92          | Predikat A                   | Predikat A                   | Berhasil   |
| `01_predikat_nilai.py`             | 84.9        | Predikat B                   | Predikat B                   | Berhasil   |
| `02_kategori_bilangan.py`          | -7          | Bilangan negatif             | Bilangan negatif             | Berhasil   |
| `02_kategori_bilangan.py`          | 8           | Bilangan positif genap       | Bilangan positif genap       | Berhasil   |
| `03_validasi_rentang.py`           | 90          | Sudut siku-siku              | Sudut siku-siku              | Berhasil   |
| `03_validasi_rentang.py`           | 180         | Pesan penolakan rentang      | Pesan penolakan rentang      | Berhasil   |
| `04_validasi_tipe.py`              | 15          | 75.00 persen dan Tuntas      | 75.00 persen dan Tuntas      | Berhasil   |
| `04_validasi_tipe.py`              | dua belas   | Pesan penolakan tipe         | Pesan penolakan tipe         | Berhasil   |
| `05_klasifikasi_segitiga_sudut.py` | 60, 60, 60  | Segitiga lancip              | Segitiga lancip              | Berhasil   |
| `05_klasifikasi_segitiga_sudut.py` | 100, 50, 40 | Pesan penolakan jumlah sudut | Pesan penolakan jumlah sudut | Berhasil   |

## Refleksi

Satu masukan tidak valid yang semula rawan terlewat adalah ketika pengguna memasukkan teks non-angka atau membiarkan input kosong. Tanpa validasi tipe menggunakan `try-except ValueError`, program akan langsung berhenti secara mendadak dengan pesan error bawaan Python (`ValueError`).

Dengan menambahkan blok `try-except`, program dapat menangkap kesalahan konversi tersebut secara aman dan memberikan pesan penolakan yang komunikatif kepada pengguna.

Selain itu, saya belajar bahwa validasi rentang dan tipe data harus dilakukan sebelum proses perhitungan agar program tidak melakukan komputasi aritmatika pada data yang tidak valid.

## Sumber dan Integritas

Program dibuat berdasarkan Bahan Ajar Pertemuan 04 (Dr. Aan Hendrayana, S.Si., M.Pd.). Kode program dan dokumentasi disusun secara mandiri, dipelajari, serta diuji menggunakan Visual Studio Code.