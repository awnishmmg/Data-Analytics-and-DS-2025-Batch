# Different Type of arguments in Python 
# Named argument
import sys 

def add(x,y): 
    print(f'x={x} and y={y}')
    return x+y
    
def main():
    result = add(10,20) #x=10 and y=20 | position depend
    print(result)
    result = add(x=20,y=10) #length = 6
    print(result)
    result = add(y=10,x=20) #length = 6 # position is not imported value is important
    print(result)


sys.exit(main())