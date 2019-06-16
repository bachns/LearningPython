# Write a Python program to get the n (non-negative integer)
# copies of the first 2 characters of a given string. Return the n copies of
# the whole string if the length is less than 2


def new_string(str, n):
    if len(str) < 2:
        return str * n
    return 1


str = input("Enter a string: ")
num = int(input("Enter a number: "))

print("New string: " + new_string(str, num))
