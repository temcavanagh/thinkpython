# Think Python solutions to go here
# Version 2.0.17
# Solutions by T Cavanagh

#2.2 Exercise
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


#2.3 Exercise
#Q1
pi = 3.1415926535897931
r = 5.0
vol = 4.0 / 3.0 * pi * r ** 3
print(vol)

#Q2
cover_price = 24.95
discount = (cover_price * (1 - 0.4))
num_books = 60
shipping = 3 + (0.75 * (num_books - 1))
print((num_books * discount) + shipping)

#Q3
easy = (8 + 15 / 60) / 60
tempo = (7 + 12 / 60) / 60
my_run = (easy + (3 * tempo) + easy)
start_time = (6 + 52 / 60)
finish_hour = (start_time + my_run)
finish_min = (finish_hour - int(finish_hour)) * 60
finish_sec = (finish_min - int(finish_min)) * 60
print(int(finish_hour), ':', int(finish_min), ':', int(finish_sec))
