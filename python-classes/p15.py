# Dynamic Type Casting : Automatic conversion of the type by looking into value.

x = input('Enter some value:')
print(x)
print(type(x)) # <class 'str'>
result = eval(x) # eval() is used by dynamic type casting
print(f'converted type : {type(result)}')



