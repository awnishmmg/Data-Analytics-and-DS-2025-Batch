# make a cubes list from odd number from 1 to 100 by using list comprehension

l = []
print('List :',l)

for i in range(1,101):
    if i%2 == 1:
        l.append(i**3)


print('List of cubes :',l)    