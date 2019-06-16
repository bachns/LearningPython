# Write a Python program to test whether a number is within 100 of 1000 or 2000


def near(n):
    near_1000 = abs(n - 1000) <= 100
    near_2000 = abs(n - 2000) <= 100
    return near_1000 or near_2000


number = int(input("Enter a number: "))
print(near(number))
