# Different Type of arguments in Python 
# default is always at last.
# default argument is also treated as Optional Argument 

import sys 

# definition
# x : mendatory 
# y : medatory 
# z : optional -> if values is supplied then i will take your value otherwise i will my default 
# value

def add(x,y,z=0):  #Positional Argument
    print(f'x={x} and y={y} and z={z}')
    return x+y+z

def main():
    # calling
    # argument = 0
    result = add(2,3)
    print('result 1:',result)

    result = add(10,20) # No value supply : z default : 0
    print('result 2:',result)
    result = add(20,10,5) # z= 0 will be replace by 5
    print('result 3:',result)
sys.exit(main())