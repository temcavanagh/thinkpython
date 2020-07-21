#Exercise 7.1. Rewrite the function print_n from Section 5.8 using iteration instead of recursion.

def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n('adcdef', 8)
print_n('qwerty', 4)


c=1
while c<101:print((c%3<1)*'Fizz'+(c%5<1)*'Buzz'or c);c+=1