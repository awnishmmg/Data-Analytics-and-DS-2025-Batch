# function can take input and product output 
# function inputs are called arguments and parameters 
# output : return 
import sys 


# Execution of main Block or block scope

def add(a,b):
    return a+b

# Execution of the code 
def main():
    result = add(10,20)
    print(f'Result = ',result)


sys.exit(main())
# No code is executed
print('This is Print Statement this not execute')
