# Local scope vs global scope
import sys 

lyari_memeber = 'rehman' # b is global scope

def displayLyari():
    india_memeber = 'hamza'  # local variable

    global lyari_memeber # Power of global keyword
    lyari_memeber = 'ranbir'
    print(f' {india_memeber} has local rule in lyari.')
    print(f' {lyari_memeber} has global Rule in lyari.') #ranbir

def lahore():
    print(f' {lyari_memeber} has global Rule in Lahor.')

def karachi():
    print(f' {lyari_memeber} has global Rule in Karachi.')


def main():
   displayLyari()
   lahore()
   karachi()

sys.exit(main())