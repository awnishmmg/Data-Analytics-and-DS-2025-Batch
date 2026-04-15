
import random as r
import sys
def mychoice(l):
    index  = r.randint(0,len(l)-1)
    return l[index]

def main():
    choice = mychoice(list(range(90,100)))
    print('Choice :',choice)
    colors = ['green','Red','Yellow','pink','blue','black','purple']
    choice = mychoice(colors)
    print('Choice :',choice)

    dice = ['1','2','3','4','5','6']
    choice = mychoice(dice)
    print('Choice :',choice)
sys.exit(main())