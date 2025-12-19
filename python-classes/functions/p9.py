# Different Type of arguments in Python 
# default is always at last.
import sys 

def add(x,y,z=0):  #Positional Argument
    print(f'x={x} and y={y} and z={z}')
    return x+y+z


def main():
    result = add(10,20) # No value supply : z default : 0
    print(result)
    result = add(20,10,5) # z= 0 will be replace by 5
    print(result)


sys.exit(main())