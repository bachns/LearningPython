# Write a Python program to compute the future value of
# a specified principal amount, rate of interest, and a number of years


def amount(princ, rate, year):
    return princ * (1 + rate * 0.01) ** year


princ = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
year = int(input("Enter number of years: "))
print("Future amount = ", amount(princ, rate, year))
