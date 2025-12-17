# Example of Special Operators :-=
# Identity Operators : is  and is not 


# This concept is related to Memory Address 
# Value same to same ---> is ---> same
# Value is not same to same ---> is not : different 

x=10
y=x 
print(x is y)
print('Memory Address of x=',id(x))
print('Memory Address of y=',id(y))


z=20
print('Memory Address of z=',id(z))
print('Memory Address of x=',id(x))
print(z is x)