# what is nan in python :-
# nan is said to Not a Number 
# nan represent if a some value is missing or undefined or that
# cannot be represened a unpresentable numeric value.

# where we will use it :-
# 1. Dat Analysis (Pandas and Numpy)
# 2. Mathematical Operations
# 3. Machine Lines Pipelines and Data Handling

# Nan is a floating point it is not python related concept.

import math as m 

print(m.nan)
print(m.isnan(m.nan))

# if you check any value it will result it to False 
# but if its is converted to float it will return True

x = float(m.nan)
print(x)
print(m.isnan(x))

y = 10 
z = float(10)
print(m.isnan(z))