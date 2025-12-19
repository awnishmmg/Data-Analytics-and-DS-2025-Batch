# Different Type of arguments in Python 
# varible length Named argument
import sys 

def add(**d): 
    print(d)
    print(type(d))
    print('keys',d.keys())
    print('values:',d.values())

def main():
    add(name='Awnish',age=50,marks=80,subject='physics',hostel=False) #length = 6 # position is not imported value is important

sys.exit(main())