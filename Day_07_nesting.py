print('🕵️‍♀️ FAKE FAN FINDER 👀')
print('-' * 22)

movie = input("What's your favorite movie? ")
if movie == "Harry Potter":
    print("Oh, really?")
    character = input("What's your favorite character? ")
    if character == "Harry":
        print("That's nice!")
        owl = input("What name does Harry Potter give to his owl? ")
        if owl == "Hedwig":
            print("That's correct!")
            ball = input("What is the name of the Quidditch ball that is enchanted to hit Harry? ")
            if ball == "Bludger":
                print("Awesome!")
                potion = input("When Harry takes the Polyjuice Potion, who does he turn into? ")
                if potion == "Goyle":
                    print("Awesome! You are purely a Harry Potter fan 🧙‍♂️")
                else:
                    print("Fake fan! ❌")
            else:
                print("Wrong answer! Fake fan! ❌")
        else:
            print("Wrong answer! Fake fan! ❌")
    else:
        print("Wrong! You're a fake fan ❌")
else:
    print("Hmm... not a Harry Potter fan? Try again another time! 👋")
