import builtins
#builtin module is an important module which contains the definition 
# all builtin function.

original_print = print
# print('This is print')
# original_print('This is Original print')

def my_print(*args,**kwargs):
    original_print('Argument Count:',len(args))
    original_print(*args,**kwargs)


builtins.print = my_print

# Now This print function with tell no of arguments 

print('Awnish','Kumar','sharma',sep=' ') # 2
print('Awnish','Kumar','sharma',sep='') # 2
print('AwnishKumar',sep='@')
print('Awnish'+'Kumar',sep='#')


print('Hello','world')
print('Hello','world',sep='-')
print('A','B','C')
print('with backslash n A','B','C',sep='\n')
# Tricky concepts.
print('without backslash n A','B','C',sep=chr(10))












