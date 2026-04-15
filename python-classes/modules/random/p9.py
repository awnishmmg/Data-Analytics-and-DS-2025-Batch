# Random Probability 
# S = {1,2,3,4,4,5,5,5,6,6,6,6,6,6,8}
# 4 => [1,1,1,2,3,6,1]
# p(8) = 1/15 
# p(6) = 1/3
# p(even) = 


import random as r
data = ['A','B','C']
fq = [0.1,0.7,0.2]

# we define k = 3
print(r.choices(data,fq,k=3))
print(r.choices(data,fq,k=1))
print(r.choices(data,fq,k=2))

print(r.choices(data,fq,k=10))