# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20


def sum_int(a, b):
    s = a + b
    if 15 < s < 20:
        return 20
    return s


print(sum_int(3, 6))
print(sum_int(10, 6))
print(sum_int(16, 7))
