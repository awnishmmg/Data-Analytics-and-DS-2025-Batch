
# Wap in python to generate the dictionary using 2 list 

l_keys =  ['a','b','c','p','q','r']
l_values = [10,20,30,100,200,300]

d = {}

for i in range(0,len(l_values)):
    d[l_keys[i]] = l_values[i]

print('d=',d)




