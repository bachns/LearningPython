# Write a Python program to check whether a specified value is contained
# in a group of values.


def isContained(number, container):
    return number in container


list = [3, 4, 5, 100, 200, 444]
typle = (5, 1111, 222, 33, 4)

print(isContained(88, list))
print(isContained(33, typle))
