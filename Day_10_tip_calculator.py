print("TIP CALCULATOR")
print()
bill = float(input("How much did you spend?"))
tip = float(input("What percent tip would you like to give?"))
people = int(input("How many people in your group?"))
answer = (bill * (1+ tip/100))/people

print("You int owe $", round(answer, 2))
