# What is Package : collection of modules in folder is called package 
# After python 3.x : it is mendatory to keep __init__.py as mendatory inside package 
# what is __init__.py  : this is special file and automatically called as soon as package is important.

from mypackage import abc as m

print(m.getGravity())

user = m.User()
name = user.getName()
print(f'The value from mypackage :{name}')