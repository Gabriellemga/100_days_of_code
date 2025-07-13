print("GRADE CALCULATOR")
print()

name_exam = input("Enter the name of the exam:")
max_score = int(input("Enter the maximum score:"))
your_score = float(input("Enter your score:"))
grade = (your_score / max_score) * 100

if grade >= 90:
  print(f"You got {grade}% wich is an A+ 😎🎊 ")
elif grade >= 80:
  print(f"You got {grade}% wich is an A 😎")
elif grade >= 70:
  print(f"You got {grade}% wich is an B 👍")
elif grade >= 60:
  print(f"You got {grade}% wich is an C 😞")
elif grade >= 50:
  print(f"You got {grade}% wich is an D 😞")
else:
  print(f"You got {grade}% wich is an U 😭")
