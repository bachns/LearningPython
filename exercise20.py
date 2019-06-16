# Write a Python program to get a string which is n (non-negative integer)
# copies of a given string.


def copy_string_n(str, n):
    new_string = ""
    for i in range(n):
        new_string += str
    return new_string


str = input("Enter a string: ")
n = int(input("Enter a number: "))
print("New string: " + str * n)
print("New string: " + copy_string_n(str, n))
