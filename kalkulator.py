while True:
    print("=====KALKULATOR SEDERHANA=====")
    angka_pertama= float(input('MASUKKAN ANGKA PERTAMA: '))
    angka_kedua= float(input('MASUKKAN ANGKA KEDUA: '))
    print("TAMBAH(+)\nKURANG(-)\nKALI(*)\nBAGI(/)")
    aritmatika=input("PILIH OPERASI ARITMATIKA!!!: ")

    if aritmatika in  ["+", "tambah"]:
     hasil = angka_pertama + angka_kedua

    
    elif aritmatika in  ["-", "kurang"]:
     hasil = angka_pertama - angka_kedua

    
    elif aritmatika in  ["*", "kali"]:
     hasil = angka_pertama * angka_kedua
     
    elif aritmatika in  ["/", "bagi"]:
        if angka_kedua != 0:
         hasil= angka_pertama / angka_kedua
        else:
          print ("JANGAN DIBAGI NOL")  
          continue

    else:
     print("MOHON MASUKKAN ARITMATIKA DENGAN BENAR")
    
    print("INI ADALAH HASIL ANDA :", hasil)    
        
    main_lagi = input("apakah anda ingin menggunakannya lagi ? y/n ")
    if main_lagi != "y":
        print("TERIMA KASIH SUDAH MENGGUNAKAN KALKULATOR SAYA :)")
        break


