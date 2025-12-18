
# generate the random list 

import random as r 
l = list(range(1,10,2))

print(l)

#randomNess : 5
for i in range(5):
    r.shuffle(l)

print(l)
