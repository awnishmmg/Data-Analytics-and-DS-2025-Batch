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
   result = add(10,20)
   print(f'The Result = {result}')

sys.exit(main())