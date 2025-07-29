print("GUESS THE NUMBER\n")

print("Totally Random One-Million-To-One\n")

import random
attempt = 1
number = random.randint(1, 1000000)

while True:
  guess = int(input("What is you guess? "))
  if guess == number:
    print("\n You is a winner ☺️☺️☺️")
    print(f"It took you {attempt} to get it correct! ")
    break
  elif guess > number:
    print("Too high\n")
  elif guess < number:
    if guess <= 0:
     print("You are out of range. End Game")
     exit()
    print("Too low\n")
  attempt += 1
