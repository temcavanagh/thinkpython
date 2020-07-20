# Exercise 6.7

def is_power(a, b):
    while a % b == 0:
        if a == b: return True
        a /= b
    return False

print(is_power(8, 2))
print(is_power(7, 2))