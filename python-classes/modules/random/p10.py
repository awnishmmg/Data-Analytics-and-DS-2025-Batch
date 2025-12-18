# Generate the list n number 
# conditions : the list will contain randoms numbers
# need we need reverse the list 

import random as r 
n = eval(input('Enter the number:'))
l = list(range(1,n+1))
print(l)

for i in l:
    r.shuffle(l)

print(l)
rev = l[::-1]
print(rev)

# r.suffle("abc")
x = [1,2,3]
r.shuffle(x)
r.shuffle(x)
print(x)

# x = 'Awnish' 
# r.shuffle(x)
# r.shuffle(x)
# print(x)

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