# Different Type of arguments in Python 
# Positional Argument 
# Named or Keyword Argument

import sys 

def add(x,y):  #Positional Argument
    print(f'x={x} and y={y}') 
    return x+y # Addition No Difference in Output because sum follows commutative law 
    #(x+y) = (y+x)


def main():
    result = add(10,20)
    print('Result 1',result)
    result = add(20,10)
    print('Result 2',result)


sys.exit(main())