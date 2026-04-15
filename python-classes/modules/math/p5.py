# floor and ciel and round

# ciel and floor both will work if no in floating point
# if the point value is exactly greater than 0 the it will work
# 2.0 ---> ciel() or floor() : Right hand side value of a decimal 
 # <whole number> . <floating point number>....

# 1.2 --> ciel() --> 2 
# 1.5 ---> ciel() --> 2
# 1.9 ---> ciel() --->2
# 1.0 ---> ciel() ---> 1

# 3,1,3.2,3.3,4,3.5,3.6,3.7,3.8,3.9,---> whole Integer -> (ciel)4 or (floor)3 

# 1.2 --> floor() --> 1 
# 1.5 ---> floor() --> 1
# 1.9 ---> floor() ---> 1
# 1.0 ---> floor() ---> 1

import math as m # module aliasing
no = 5.67

print(f'round of for 1st significant figure: {round(no,1)}') # globally available.
print(f'round of for 2nd significant figure: {round(no,3)}')
print(f'round of : {round(no)}')

print(f'floor of : {m.floor(no)}') #5
print(f'ciel of : {m.ceil(no)}') #6

x = 2.0  # ciel -> 2 and floor - 2
print(f'ciel of = {m.ceil(x)}')
print(f'floor of = {m.floor(x)}')

print(m.ceil(2.0) == m.floor(2.0)) # True

# ciel and floor in -ve Number 
print(f'+ve 2.5 ciel = ',m.ceil(2.5))
print(f'-ve 2.5 ciel = ',m.ceil(-2.5))

# <---------------3-2.5-2-------------0---------------2-2.5-3------------->

print(f'+ve 2.5 floor = ',m.floor(2.5)) # 2
print(f'-ve 2.5 floor = ',m.floor(-2.5)) # -3







