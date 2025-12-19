# Different Type of arguments in Python 
# varaible length argument : we can supply n of arguments
import sys 

def add(*n):  #Positional Argument
    print(n)
    print(type(n))
    print(len(n))
    sum = 0
    for i in n:
        sum = sum+i
    return sum
    
def main():
    result = add(20,10,5,6,7) #length = 6
    print(result)


sys.exit(main())