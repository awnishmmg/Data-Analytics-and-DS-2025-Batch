# make a cubes list from odd number from 1 to 100 by using list comprehension

l = [i**3 for i in range(1,101) if i%2 == 1 ]
print('List :',l)

