
# Named or Keyword Argument : in Named Argument we refer the value by name not by position.
# we will explicitly say x=10 y=20
# in named argument it does not depend on the value.

import sys 

def add(x,y):  #Named Argument
    print(f'x={x} and y={y}') 
    return x+y # Addition No Difference in Output because sum follows commutative law 
    #(x+y) = (y+x)


def main():
    result = add(x=10,y=20)
    print('Result 1',result)
    result = add(y=20,x=10)
    print('Result 2',result)


sys.exit(main())