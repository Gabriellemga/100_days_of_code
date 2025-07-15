print("Animal Sound Machine: What's That Sound?\n")

exit = ""

while exit != "yes":
  animal = input("What animal do you want? ")
  if animal == "Cow" or animal == "cow":
    print("A cow goes moo 🐮")
  elif animal == "Pig" or animal == "pig":
    print("A pig goes oink  🐷")
  elif animal == "Duck" or animal == "duck":
    print("A duck goes quack 🦆")
  elif animal == "Cat" or animal == "cat":
    print("A cat goes meow 😸")
  elif animal == "Dog" or animal == "dog":
    print("A dog goes wook  🐶")
  elif animal == "Sheep" or animal == "sheep":
    print("A sheep goes baa 🐑")
  elif animal == "Horse" or animal == "horse":
    print("A horse goes neigh  🐴")
  elif animal == "Lion" or animal == "lion":
    print("A lion goes roar 🦁")
  elif animal == "Rabbit" or animal == "rabbit":
    print("A rabbit goes snuffle 🐰")
  exit = input("\nDo you want to exit? ")
  if exit == "yes" or exit == "Yes":
    print("Goodbye  😃")
