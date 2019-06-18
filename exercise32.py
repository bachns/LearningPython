# Write a Python program to get the least common multiple (LCM)
# of two positive integers


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


a = int(input("Enter number A = "))
b = int(input("Enter number B = "))
print("LCM(A, B) = %d" % lcm(a, b))
