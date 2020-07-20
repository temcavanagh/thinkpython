# The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

print(gcd(20, 8))
print(gcd(99, 45))