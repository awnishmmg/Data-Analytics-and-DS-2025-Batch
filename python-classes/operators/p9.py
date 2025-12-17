# Example of Special Operators :-=
# isinstance : it tell wheather a Percular element is an Object that Class  

name = 'Awnish'
print(type(name))
print(isinstance(name,str)) #true
print(isinstance(10,str)) #false

print(isinstance(10,int)) #true
print(isinstance({'age':20,'name':'Ravi'},str)) #false
print(isinstance({'age':20,'name':'Ravi'},dict)) #true