print("Infinity Dice  🎲\n")

import random

sides = int(input("How many sides?"))
def roll_dice(sides):
  while True:
    roll = random.randint(1, sides)
    print("You rolled ", roll, "\n")
    again = input("Roll again?")
    if again == "yes":
      continue
    elif again == "no":
      print("Goodbye!")
      break
    else:
      print("Invalid input,please enter 'yes' or 'no'")
      again = input("\nRoll again?")
      
roll_dice(sides)
