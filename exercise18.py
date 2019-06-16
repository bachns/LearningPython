# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum


def sum(a, b, c):
    s = a + b + c
    if a == b and b == c:
        return 3 * s

    return s


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

print("Result: " + str(sum(first, second, third)))
