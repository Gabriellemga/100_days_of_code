print("HOW MANY SECONDS ARE IN A YEAR?\n")

year = int(input("Enter the number of year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  seconds = 60 * 60  * 24 * 366
  print("This year have", seconds, "seconds")
else:
  seconds = 60 * 60  * 24 * 365
  print("This year have", seconds, "seconds")
