
import os
import sys 


print('This is Test File')
print('value of name variable:',__name__)
print('value of file variable',os.path.basename(__file__))
print('value from argv:',sys.argv[0])