def square_root(a):
    x = a / 2.0
    while True:
        print(x)
        y = (x - (a/x) / 2)
        if x == y:
            break
        x = y

print(square_root(9.0))