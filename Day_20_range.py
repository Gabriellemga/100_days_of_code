print("List Generator\n")

start = int(input("Start at?"))
end = int(input("End before?"))
step = int(input("Increment values?"))

for i in range(start, end, step):
  print(i)
