# Write a Python program to concatenate all elements in a list into
# a string and return it


def concatenate(list):
    conc_str = ""
    for number in list:
        conc_str += str(number)

    return conc_str


print(concatenate([3, 4, 1000, 23, 2]))
