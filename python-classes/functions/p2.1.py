# function can take input and produce output 
# function inputs are called arguments and parameters 
# output : return 
import sys 

# Execution of main Block or block scope
# take input a and b and return the sum
def add(a,b):
    return a+b

# Execution of the code 
def main():
    a = int(input('Enter the a value:'))
    b = int(input('Enter the b value:'))
    result = add(a,b)
    print(f'Result = ',result)

sys.exit(main())
# No code is executed
print('This is Print Statement this not execute')
