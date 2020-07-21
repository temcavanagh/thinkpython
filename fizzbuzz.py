c=1
while c<101:
    print((c%3<1)*'Fizz'+(c%5<1)*'Buzz'or c)
    c+=1