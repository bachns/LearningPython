# Write a Python program to calculate number of days between two dates.
# Sample dates : (2019, 7, 2), (2019, 7, 11)
# Expected output : 9 days

from datetime import date

begin = date(2019, 7, 2)
end = date(2019, 7, 11)
delta = end - begin

print("Number of days between two dates: " + str(delta.days))
