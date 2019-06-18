# Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero


def sum_int(a, b, c):
    if a == b or b == c or a == c:
        return 0
    return a + b + c


print(sum_int(3, 4, 5))
print(sum_int(3, 3, 5))
print(sum_int(3, 5, 3))
print(sum_int(5, 3, 3))
print(sum_int(33, 22, 11))
