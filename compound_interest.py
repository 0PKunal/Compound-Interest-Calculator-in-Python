# A program to calculate compound interest(I)

#Input from user
P = float(input("Enter the principal amount(P): "))
r = float(input("Enter the interest rate(r in %): "))
t = float(input("Enter the time(t in years): "))

#Calculate the amount
A = P * (1 + r / 100) ** t

#Calculate the interest
I = A - P

#Show the calculations
print(f"\nCompound Interest(I) = {I:.2f}")
print(f"Total AMount (A) after (t) years = {A:.2f}")