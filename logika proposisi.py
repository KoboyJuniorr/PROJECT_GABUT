print(" \n\n           ~~~~~ SELAMAT DATANG DI PROGRAM LOGIKA PROPOSISI ~~~~~ \n\n ")

#menampilkan tampilan tabel kebenaran

print('''
------------------------- T A B E L _____________ K E B E N A R A N ------------------------      

[   p  ] [   q  ]  [   ~q   ] [   p and q   ] [   p or q   ] [   p -> q    ] [   p <-> q   ]
      
[   B  ] [   B  ]  [    S   ] [      B      ] [      B     ] [      B      ] [      B      ]
[   B  ] [   S  ]  [    B   ] [      S      ] [      B     ] [      S      ] [      S      ]
[   S  ] [   B  ]  [    S   ] [      S      ] [      B     ] [      B      ] [      S      ]  
[   S  ] [   S  ]  [    S   ] [      S      ] [      S     ] [      B      ] [      B      ]         
     
silahkan memilihin metode :
      
    1. not 
    2. and
    3. or
    4. implikasi
    5. bimplikasi
\n
''')

pilihan = int(input("masukkan pilihan anda : "))

if pilihan == 1 :
    a = str(input("masukkan nilai  : "))
    if a == "b" :
        print("hasil dari nilai not = S ")
    else :
        print("hasil dari nilai not = B")

elif pilihan == 2 :
    a = str(input("masukkan nilai ke-1 : "))
    b = str(input("masukkan nilai ke-2 : "))
    if a == "b" and b == "b":
        print("hasil dari nilai 'and' nya adalah B")
    else:
        print("HASIL DARI NILAI 'and NYA ADALAH S")
elif pilihan == 3 :
    a = str(input("masukkan nilai ke-1 : "))
    b = str(input("masukkan nilai ke-2 : "))
    if a == 'b' and b == 's' or  a == 's' and b == 'b':
        print("hasil dari nilai 'or' nya adalah B")
   
    else :
        print("hasil dari nilai 'or' nya adalah S")    

elif pilihan == 4 :
    a = str(input("masukkan nilai ke-1 : "))
    b = str(input("masukkan nilai ke-2 : "))
    print("hasil dari 'implikasi' nya adalah ",b)

elif pilihan == 5 :
    a = str(input("masukkan nilai ke-1 : "))
    b = str(input("masukkan nilai ke-2 : "))
    if a == 'b' and b == 'b' or a == 's' and b == 's' :
        print("hasi dari 'bimplikasi' nya adalah B")
    else :
        print("hasi dari 'bimplikasi' nya adalah B")

else:
    print("pilihan tidak terdaftar")