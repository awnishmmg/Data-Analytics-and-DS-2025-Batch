# Different Type of arguments in Python 
# How to return the multiple values in python
import sys 

def getDictionary():
    return {'name':'Awnish','age':50}

def getList(): 
    return [10,20]

def getTuple():
    return (10,20,30)

def getMutiple():
    return 100,200,300  # tuples


def main():
    result = getList()
    print(f'The Result = {result}')
    print(f'Returning as dict :',getDictionary())
    print(f'Returning as tuple :',getTuple())
    print(f'Returning as Multiple Values :',getMutiple())
    print(f'Returning as Multiple Values :',type(getMutiple()))

sys.exit(main())