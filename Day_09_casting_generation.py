print("GENERATION IDENTIFIER\n")

year = int(input("Which year were you born? "))

if year >= 1883 and year <= 1900:
  print("\nHah! 🌪️ Lost Generation:Witnessed empires fall and fashion rise... definitely didn’t ask for an encore.")
elif year >= 1901 and year <= 1927:
  print("\nHah!🎩 Greatest Generation. Survived the Great Depression and won wars. Heroes with vintage flair")
elif year >= 1928 and year <= 1945:
  print("\n🕺 Silent Generation. Few tweets, loads of wisdom. Quiet but mighty!")
elif year >= 1946 and year <= 1964:
  print("\n✌️ Baby Boomers.Led revolutions, wore bell-bottoms, and still know how to open a PDF.")
elif year >= 1965 and year <= 1980:
  print("\n🧃 Generation X. Between cassette tapes and Wi-Fi: true masters of adaptation.")
elif year >= 1981 and year <= 1996:
  print("\n📼 Millenials. Raised on Pokémon and dial-up.\n Now rule the world (with coffee).")
elif year >= 1997 and year <= 2012:
  print("\n📱 Generation Z. Born influencers. Weak Wi-Fi = identity crisis.")
elif year >= 2013:
  print("\n🍼Generation Alpha. Born knowing how to swipe.\n Just want more battery and fewer limits.")
else:
  print("\nPlease! Enter a valid year.")
