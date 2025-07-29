print("Math Game !\n")

number = input("Name your multiples:")
print()
score = 0

for i in range(1, 11):
   print(f"{i} x {number} = ")
   count = int(i) * int(number)
   answer = int(input(" "))
   if answer == int(i) * int(number):
     score += 1
     print("Great work!\n")
   else:
     print("Nope! 😢 The answer is", count ,"\n")
if score == 10:
  print("You got a perfect score!")
else:
  print("You scored ", score, "out of 10!!! 🎉🎉🎉")
