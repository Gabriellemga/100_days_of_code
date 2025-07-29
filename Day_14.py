print("EPIC ✂️  📄 ⛰️  BATTLE")
print("*" * 20)
print()

from getpass import getpass as input

print("Select your move (R, P or S)\n")
player1 = input("Player 1 -> ")
player2 = input("Player 2 -> ")

if player1 == player2:
  print("\nIt's a tie! 😉")
elif player1 == "R":
  if player2 == "S":
    print("\nPlayer1's rock ⛰️  beats Player2's scissors ✂️")
  else:
    print("\nPlayer2's paper 📄 smothered Player1's rock ⛰️")
elif player1 == "P":
  if player2 == "R":
    print("\nPlayer1's paper 📄 smothered Player2's rock ⛰️")
  else:
    print("\nPlayer2's scissors ✂️  cut Player1's paper 📄")
elif player1 == "S":
  if player2 == "P":
    print("\nPlayer1's scissors ✂️  cut Player2's paper 📄")
  else:
    print("\nPlayer2's rock ⛰️  beats Player1's scissors ✂️")
    
