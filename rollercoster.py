while True:
    print("====== SELAMAT DATANG DI WAHANA ROLLER COSTER =====")
    print("PERATURAN WAHANA\n1.MINIMAL BERUSIA 15 TAHUN\n2.TINGGI MINIMAL 150 CM\n3.TIDAK ADA RIWAYAT PENYAKIT")
    usia = float (input ("Masukkan usia anda: "))
    tinggi = float (input ("Masukkan tinggi anda: "))
    sakit = input ("APAKAH ADA RIWAYAT SAKIT? :y/n ").lower()

    if usia >= 15 and tinggi >= 150 and sakit == "n":
        print("\n✅ Anda memenuhi syarat. Selamat menikmati wahana!")
    else:
            print("\n❌ Maaf, Anda tidak diperbolehkan naik wahana.")
    print("Alasan:")
    if usia < 15:
        print("- Usia kurang dari 15 tahun")
    if tinggi < 150:
        print("- Tinggi kurang dari 150 cm")
    if sakit != "n":
        print("- Ada riwayat penyakit")