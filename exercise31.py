# Write a Python program to compute the greatest common divisor (GCD)
# of two positive integers.


# Solution 1
def gcd1(a, b):
    if b == 0:
        return a
    return gcd1(b, a % b)


# Solution 2
def gcd2(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a = int(input("Enter number A = "))
b = int(input("Enter number B = "))
print("GCD_solution1(A, B) = ", gcd1(a, b))
print("GCD_solution2(A, B) = ", gcd2(a, b))
