# Different Type of arguments in Python 
# varible length Named argument
import sys 

def add(**d): 
    print(d)
    return d['x'] + d['y']
    
def main():
    result = add(y=10,x=20) #length = 6 # position is not imported value is important
    print(result)


sys.exit(main())