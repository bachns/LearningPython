# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5


def check(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5


print(check(7, 2))
print(check(3, 2))
print(check(2, 2))
