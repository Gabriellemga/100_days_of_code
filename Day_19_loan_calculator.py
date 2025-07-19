print("Loan Calculator\n")
print("$ 1000 over 10 years at 5% APR\n")

loan = 1000
apr = 0.05
years = 10

for year in range(1,11):
  loan  *= 1 + apr
  print(f"Year {year} is {loan:.2f}")
print(f"\nYou paid $ {loan-1000:.2f} in interest!!")
