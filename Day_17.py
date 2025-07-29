print("EPIC ✂️  📄 ⛰️  BATTLE\n")


from getpass import getpass as input

round = 1
score_player1 = 0
score_player2 = 0

while True:
  print("*" * 50)
  print("<>Round", round, "<>\n")
  print("Select your move (R, P or S)\n")
  player1 = input("Player 1 -> ")
  player2 = input("Player 2 -> ")
  
  if player1 == player2:
    print("\nIt's a tie! 😉")
  elif player1 == "R":
    if player2 == "S":
      print("\nPlayer1's rock ⛰️  beats Player2's scissors ✂️")
      score_player1 += 1
    else:
      print("\nPlayer2's paper 📄 smothered Player1's rock ⛰️")
      score_player2 += 1
  elif player1 == "P":
    if player2 == "R":
      print("\nPlayer1's paper 📄 smothered Player2's rock ⛰️")
      score_player1 += 1
    else:
      print("\nPlayer2's scissors ✂️  cut Player1's paper 📄")
      score_player2 += 1
  elif player1 == "S":
    if player2 == "P":
      print("\nPlayer1's scissors ✂️  cut Player2's paper 📄")
      score_player1 += 1
    else:
      print("\nPlayer2's rock ⛰️  beats Player1's scissors ✂️")
      score_player2 += 1
  round += 1

  if score_player1 == 3:
    print("\nPlayer1 wins the game with three victories!!!")
    break
  elif score_player2 == 3:
    print("\nPlayer2 wins the game with three victories!!!")
    break
