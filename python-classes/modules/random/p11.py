import random as r

# s = r.shuffle('Awnish') # Invalid str is Not Iterable in suffle.
# str -> list  -> shuffle -> join 
x = list('Awnish')
print('original x with str with list',x)
r.shuffle(x)
r.shuffle(x)
print('Suffle String :',"".join(x))

# How to Join str without using Join() function 
# =================================================

x = 'Awnish'
y = list(x)
print(y)

r.shuffle(y)
r.shuffle(y)
print(y)

s = ""
for i in y:
  s = s + i

print(s)