# Type Hinting 
# Even thougt we donot declare type in python , # but after 3.5 version
# python allows you declare type 

x : str = 'Awnish'
print(x)
print(type(x))

x=10
print(x)
print(type(x))

x:int=10 # type -> int 
print(x)
print(type(x))

from typing import Union

x:Union[str,int] = 'Awnish'
print(x)
print(type(x))


