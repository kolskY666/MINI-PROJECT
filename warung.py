def judul_program(teks):
    garis = "=" * len(teks)
    return f"{garis}\n{teks.upper()}\n{garis}"

# Tampilan awal
print(judul_program("WARUNG LALAPAN KHAS MADURA"))
print("Daftar Menu dan Harga:")
print(judul_program("Makanan"))
print("Ayam bumbu hitam: 18.000\nBebek bumbu hitam: 20.000\nNasi: 5.000\nTahu tempe: 3.000")
print(judul_program("Minuman"))
print("Es teh: 4.000\nEs jeruk: 4.000\nEs degan: 5.000")
print("\nKetik 'selesai' jika sudah cukup.\n")

# List untuk menyimpan pesanan
pesanan_list = []
jumlah_list = []
harga_list = []

# Input pesanan
while True: 
    pesan = input("Masukkan yang ingin Anda pesan: ").lower()
    if pesan == 'selesai':
        break
    try:
        jumlah = int(input("Masukkan jumlah: "))
        harga = int(input("Masukkan harga: "))
    except ValueError:
        print("Masukkan angka yang benar!\n")
        continue
        
    pesanan_list.append(pesan)
    jumlah_list.append(jumlah)
    harga_list.append(harga)

# Menampilkan struk belanja
print("\n" + judul_program("STRUK PEMBELIAN"))
total = 0        
for i in range(len(pesanan_list)):
    subtotal = jumlah_list[i] * harga_list[i]
    total += subtotal
    print(f"{pesanan_list[i].title()} ({jumlah_list[i]} x {harga_list[i]:,}) = {subtotal:,}")

print(f"\nTotal yang harus dibayar: {total:,}")













































































































































































































