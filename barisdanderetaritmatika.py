print ('''
=================================================================
|                                                               |
|     SELAMAT DATANG DI PROGRAM BARIS DAN DERET ARITMATIKA      |
|                       by KoboyJuniorr                         |
=================================================================                  

''')
print("1. mencari nilai Un jika a dan b diketahui ")
print("2. mencari nilai Un jika a dan b tidak diketahui \n")
#print("3. mencari nilai jumlah total suku  \n")
pilihan = int(input("masukkan pilihan anda : "))
if pilihan == 1 :
  n = int(input("masukkan nilai Un yang mau di cari :"))
  a = int(input("masukkan nilai a :"))
  b = int(input("masukkan nilai b :"))
  ub= a + (n-1) * b
  print("===========================\n  ")
  print(" nilai U",n," = ",ub)

elif pilihan == 2 :

    u1 = int(input("masukkan suku pertama yang diketahui :"))
    u2 = int(input("masukkan suku kedua yang diketahui :"))
    nup = int(input("masukkan nilai suku pertama yang diketahui :"))
    nud = int(input("masukkan nilai suku kedua yang diketahui :"))
    un = int(input("masukkan suku yang ingin dicari :"))


    up = u1 - 1 
    ud = u2 - 1

    hasiln = nup - nud
    hasilu = up - ud

    b = hasiln / hasilu

    a = nup - (up*b)

    uhasil = a + (un-1) * b
    print("\n\n =================================== \n")    
    print("beda yang didapatkan adalah = ",b)
    print("nilai awal didapatkan adalah = ",a)
    print("suku ke- ",un, " yang didapatkan adalah = ",uhasil)

