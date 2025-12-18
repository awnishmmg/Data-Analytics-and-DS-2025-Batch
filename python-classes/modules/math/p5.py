# floor and ciel and round

# ciel and floor both will work if no in floating point
# if floating point is <0 if it is zero it wont work 
# 1.2 --> ciel() --> 2 
# 1.5 ---> ciel() --> 2
# 1.9 ---> ciel() --->2
# 1.0 ---> ciel() ---> 1


# 1.2 --> floor() --> 1 
# 1.5 ---> floor() --> 1
# 1.9 ---> floor() ---> 1
# 1.0 ---> floor() ---> 1


import math as m
no = 5.67
print(f'round of : {round(no,1)}')
print(f'floor of : {m.floor(no)}')
print(f'ciel of : {m.ceil(no)}')

x = 2.0 
print(f'ciel of = {m.ceil(x)}')
print(f'floor of = {m.floor(x)}')








