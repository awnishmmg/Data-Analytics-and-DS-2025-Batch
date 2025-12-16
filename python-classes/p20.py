# How to make the code typecheck Mendatory in python 

import os 
import sys

def main():
    x:int = input('Enter the x value:')
    print(x)

os.system(f'python -m mypy {sys.argv[0]}')
