import random

bot = ["batu", "gunting" , "kertas"]
while True:

  computer = random.choice(bot)
  print('''
================================
====== Welcome To The Game =====
================================
=             batu             =
=            gunting           =
=            kertas            =
================================''')
  player = input('masukkan pilihan mu :')
  if player == computer:
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|         Draw          |")
    print("=========================")
    
  #bagian menang
  elif player == "batu" and computer == "gunting":
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|         Win           |")
    print("=========================")
  elif player == "gunting" and computer == "kertas":
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|         Win           |")
    print("=========================")
  elif player == "kertas" and computer == "batu":
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|          Win          |")
    print("=========================")
    
    
    #bagian kalah 
  elif player == "batu" and computer == "kertas":
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|         Lose          |")
    print("=========================")
  elif player == "gunting" and computer == "batu":
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|         Lose          |")
    print("=========================")
  elif player == "kertas" and computer == "gunting":
    print(f'your choice == {player}')
    print("            VS          ")
    print(f'computer  == {computer}')
    print("=========================")
    print("|         Lose          |")
    print("=========================")
  else:
    print("pilihan tidak ada dalan daftar")

