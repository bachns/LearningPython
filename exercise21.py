# Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user


def check_number(number):
    if number % 2:
        return "This is an odd number"
    return "This is an even number"


number = int(input("Enter a number: "))
print(check_number(number))
