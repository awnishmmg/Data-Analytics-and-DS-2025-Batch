# Type of function on the basis of argument and return type 

# ================= 4 Types are there =======================
# No Argument and No Return Type 
# with Argument and No Return type 
# No Argument with Return Type
# with Argument with Return Type 


# No Argument and with Return Type 
import sys

def getGravity():
    return 9.8 


def main():
    print(f'The value of the gravity:{getGravity()}')

sys.exit(main())