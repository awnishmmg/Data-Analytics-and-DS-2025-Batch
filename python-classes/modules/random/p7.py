
# we know that the more you call suffle() the more it becomes random so instead calling 
# of multiples times use for loop()

import random as r 
l = list(range(1,10,2))

print(l)

#randomNess : 5 : Entropy
for i in range(5):
    r.shuffle(l)

print(l)
