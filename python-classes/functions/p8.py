# Different Type of arguments in Python 
import sys 

def add(x,y):  #Positional Argument
    print(f'x={x} and y={y}')
    return x+y


def main():
    result = add(10,20)
    print(result)
    result = add(20,10)
    print(result)


sys.exit(main())