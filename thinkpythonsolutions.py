# Think Python solutions to go here
# Version 2.0.17
# Solutions by T Cavanagh

# 2.2 Exercise
width = 17
height = 12.0
delimiter = '.'

q1 = width / 2
print(q1)
print(type(q1))

q2 = width / 2.0
print(q2)
print(type(q2))

q3 = height / 3
print(q3)
print(type(q3))

q4 = 1 + 2 * 5
print(q4)
print(type(q4))

q5 = delimiter * 5
print(q5)
print(type(q5))


# 2.3 Exercise
# Q1
pi = 3.1415926535897931
r = 5.0
vol = 4.0 / 3.0 * pi * r ** 3
print(vol)

# Q2
cover_price = 24.95
discount = (cover_price * (1 - 0.4))
num_books = 60
shipping = 3 + (0.75 * (num_books - 1))
print((num_books * discount) + shipping)

# Q3
easy = (8 + 15 / 60) / 60
tempo = (7 + 12 / 60) / 60
my_run = (easy + (3 * tempo) + easy)
start_time = (6 + 52 / 60)
finish_hour = (start_time + my_run)
finish_min = (finish_hour - int(finish_hour)) * 60
finish_sec = (finish_min - int(finish_min)) * 60
print(int(finish_hour), ':', int(finish_min), ':', int(finish_sec))

# Exercise 3.3

def right_justify(s):
    leading = 70 - len(s)
    return " " * leading + s

print(right_justify("python"))

# Exercise 3.4

def do_twice(f, val):
    f(val)
    f(val)

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

def print_twice(s):
    print(s)
    print(s)

do_four(print_twice, "spam")

# Exercise 3.5

def grid(n):
    filled = "+ - - - - "
    empty = "|         "
    grid = ""

    for i in range(n):
        grid += filled * n + filled[0] + "\n"
        grid += 4 * (empty * n + empty[0] + "\n")

    grid += filled * n + filled[0] + "\n"

    return grid

print(grid(2))
print(grid(4))

# Exercise 5.3

def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def fermat_input():
    a = int(input("Please enter a: "))
    b = int(input("Please enter b: "))
    c = int(input("Please enter c: "))
    n = int(input("Please enter n: "))
    check_fermat(a, b, c, n)

fermat_input()

#Exercise 5.4

def is_triangle(a, b, c):
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Yes")

def prompt():
    a = input("Enter length of side a: ")
    b = input("Enter length of side b: ")
    c = input("Enter length of side c: ")
    
    is_triangle(int(a), int(b), int(c))
    
prompt()   

