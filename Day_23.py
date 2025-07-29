print("Replit Login System")
print("--------------------")

def login():
  while True:
    username = input("\nWhat is your username? ")
    password = input("What is your password? ")
    if username == "admin" and password == "replitlife88":
     print("\nWelcome to Replit!!")
     break
    else:
     print("\nWhoops, I don't recognize that username or password. Try again!!")
     continue
  

login()
