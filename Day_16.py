print("Fill-in the blanks Lyrics")
print("type in the blank lyrics and see if you're as cool as me.\n")

conter = 0
while True:
  print("Break down, only alone I will ___ out now\n")
  aswer = input("Fill in the blank lyrics:")
  conter += 1
  if aswer == "cry":
    print("You win! 😄🤩")
    break
  elif aswer != "cry":
    print("Nope, try again!\n")
    if conter == 3:
       print("You lose!😪😪😪.It only took you 3 attempts")
       break
