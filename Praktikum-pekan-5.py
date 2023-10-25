kendaraan = ["fortuner","mobil",2000,"hitam",4]
kendaraan.append("500jt,SUV")
kendaraan.insert(1,"toyota")
print(kendaraan)
print()

print("1.luas persegi")
print("2.luas lingkaran")
print("3.luas segitiga")
pilih = int(input("Masukkan pilihan Anda: "))

    
match pilih:
    case 1:
        sisi = int(input("Masukkan panjang sisi persegi: "))
        luas1 = int(sisi * sisi)
        print("Luas persegi adalah" ,(luas1) )
    case 2:
        radius = float(input("Masukkan radius lingkaran: "))
        luas2 = 3,14 * (radius ** 2)
        print("Luas lingkaran adalah ",(luas2) )
    case 3:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas3 = int(0.5 * alas * tinggi)
        print("Luas segitiga adalah", (luas3))
    case _:
         print("Pilihan tidak valid")


