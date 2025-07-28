print("⚔️  Character Stats Generator  ⚔️")

import random 

def dice_roll(sides):
  return random.randint(1,sides)

def health_character():
   name = input("\nName your warrior:")
   health = (dice_roll(6) * dice_roll(8))
   print("Their health is:", health,"hp")

new_character = input("\nDo you want to generate a character?")
while True:
  if new_character == "no":
      print("Goodbye!!!")
      exit()
  elif new_character == "yes":
      health_character()
  new_character = input("\nDo you want to generate a new character?")
