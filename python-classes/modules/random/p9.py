# Random Probability 

import random as r
data = ['A','B','C']
fq = [0.1,0.7,0.2]

# we define k = 3
print(r.choices(data,fq,k=3))