# randomrange : randomrange is same as random but it generate the random 
# list 

import random as r 

l = list(range(90,100))
# l = ['a','b','c','d','e','f','g','h']
print(l)
print('min length:',0)
print('max length:',len(l))
index  = r.randint(0,len(l))
print('random Index:',index)

print('Random Element from list l:',l[index])
import random as r 
print(r.randrange(90,100))

print(list(range(90,100,2)))
print(r.randrange(90,100,2))

