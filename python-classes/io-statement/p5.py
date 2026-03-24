#wap in python to show case end and sep both 

print('Awnish','Kumar',sep='-',end='!')
print('Awnish','Kumar',end='!',sep='-')

# 'Awnish','Kumar' : Position Argument : Position matters
print('Awnish','Kumar',sep='-',end='!')
print('Kumar','Awnish',end='!',sep='-')
#named arguments (sep,end,flush) : name argument : if we change the position output does not effect.