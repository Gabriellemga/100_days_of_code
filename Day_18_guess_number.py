print("GUESS THE NUMBER\n")

print("One-Million-To-One\n")

attempt = 1

while True:
  number = 350
  guess = int(input("What is you guess? "))
  if guess == 350:
    print("You is a winner ☺️☺️☺️")
    print(f"It took you {attempt} to get it correct! ")
    break
  elif guess > 350:
    print("Too high\n")
  elif guess < 350:
    if guess <= 0:
     print("You are out of range. End Game")
     exit()
    print("Too low\n")
  attempt += 1
