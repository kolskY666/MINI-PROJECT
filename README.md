
# 🐔 Warung Lalapan Khas Madura

Aplikasi kasir sederhana berbasis teks untuk menghitung total pesanan di warung makan.

## 📌 Deskripsi

Program ini digunakan untuk mencatat pesanan makanan/minuman pelanggan di sebuah warung makan. Pengguna akan memasukkan pesanan, jumlah, dan harga satuan, lalu program akan menghitung total belanja dan mencetak struk sederhana.

## 🎯 Fitur

- Menampilkan menu makanan dan minuman.
- Input pesanan secara fleksibel sampai mengetik `selesai`.
- Menyimpan data pesanan, jumlah, dan harga.
- Menampilkan struk belanja dengan perhitungan subtotal dan total.
- Format harga otomatis dalam ribuan (contoh: 18,000).

## ▶️ Cara Menjalankan

1. Buka terminal atau Command Prompt.
2. Jalankan file Python:
   ```bash
   python warung_lalapan.py
   ```
3. Ikuti petunjuk input:
   - Masukkan nama pesanan
   - Masukkan jumlah
   - Masukkan harga satuan
   - Ketik `selesai` jika sudah cukup

## 📦 Contoh Output

```
=======================================
WARUNG LALAPAN KHAS MADURA
=======================================
Daftar Menu dan Harga:
=======================================
MAKANAN
=======================================
Ayam bumbu hitam: 18.000
Bebek bumbu hitam: 20.000
...
Masukkan yang ingin Anda pesan: ayam bumbu hitam
Masukkan jumlah: 2
Masukkan harga: 18000
...

=======================================
STRUK PEMBELIAN
=======================================
Ayam Bumbu Hitam (2 x 18,000) = 36,000
...
Total yang harus dibayar: 36,000
```

## 🛠️ Teknologi

- Python 3
- Terminal/Command Line

## 📚 Pembelajaran yang Diperoleh

- Menggunakan list untuk menyimpan data dinamis
- Menggunakan loop dan kondisi
- Penanganan error dengan `try-except`
- Perhitungan matematika sederhana
- Format string dan tampilan user-friendly

---

✅ Cocok untuk latihan Python dasar seperti:
- `input()`, `print()`, `if`, `while`, `for`, `list`, dan `function`

---

## 📈 Rencana Pengembangan

- Menambahkan validasi menu
- Menyimpan struk ke file `.txt`
- Menambahkan sistem admin dan pelanggan
- Menambahkan fitur diskon/pajak
