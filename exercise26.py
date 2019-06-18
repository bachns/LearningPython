# Write a Python program to create a histogram from a given list of integers


def histogram(list):
    for num in list:
        str = ""
        for i in range(num):
            str += "*"
        print(str)


histogram([5, 6, 8, 10, 9, 7, 4, 3, 2, 2, 3, 4])
