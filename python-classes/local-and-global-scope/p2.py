# Local scope vs global scope
import sys 

lyari_memeber = 'rehman' # b is global scope

def displayLyari():
    india_memeber = 'hamza'  # local variable
    lyari_memeber = 'ranbir'
    print(f' {india_memeber} has local rule within Lyari')
    print(f' {lyari_memeber} has global Rule within Lyari') #ranbir


def lahore():
    print(f' {lyari_memeber} has global Rule in Lahore')


def main():
   displayLyari()
   lahore()

sys.exit(main())