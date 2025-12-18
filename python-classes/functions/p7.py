# Type of function on the basis of argument and return type 

# ================= 4 Types are there =======================
# No Argument and No Return Type 
# with Argument and No Return type 
# No Argument with Return Type
# with Argument with Return Type 

# with Argument and No Return Type 
import sys

def add(x,y):
   return x+y

def main():
   no1 = eval(input('Enter the first No:')) 
   no2 = eval(input('Enter the 2nd No:'))
   result = add(no1,no2)
   print(f'The Result = {result}')

sys.exit(main())