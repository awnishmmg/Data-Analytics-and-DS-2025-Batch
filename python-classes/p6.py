
#How to use print 
print('Awnish')
print("Awnish Kumar")
x=10
print(x)

print('x=',x) #comman seperated values
print('x='+str(x)) # concatenation


x=10
name = 'Ravi'
age = 20
print('x=',x,'name=',name,'age=',age)
print(f'x={x} name={name} age={age}') #format string or fstring

# .format() string
print('x={x} name={name} age={age}'.format(x=x,name=name,age=age))
print('x={a} name={b} age={c}'.format(a=x,b=name,c=age))

print('x={} name={} age={}'.format(x,name,age))
print('x={} name={} age={}'.format(age,name,x))
