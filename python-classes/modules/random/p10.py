# Generate the list n number 
# conditions : the list will contain randoms numbers
# need we need reverse the list 

import random as r 
n = eval(input('Enter the number:'))
l = list(range(1,n+1))
print('original List:',l)

for i in l:
    r.shuffle(l)

print('shuffled list:',l)
rev = l[::-1]
print('Reserved List',rev)

x = [1,2,3]
print('Original x:',x)
r.shuffle(x)
r.shuffle(x)
print('shuffled x:',x)
