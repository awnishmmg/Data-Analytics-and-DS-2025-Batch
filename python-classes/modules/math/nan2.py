import numpy as np 

#print(np.__version__)
x = np.nan 
print(x)

A = np.array([10,20,30,x,40]) # Analysis 
print(np.isnan(A))