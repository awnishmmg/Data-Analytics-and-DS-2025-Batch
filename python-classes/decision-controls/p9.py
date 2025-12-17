# Make a Program for Odd and Even 
# No --> Divider --> Remainder 
# Remainder -> 0,1
# Remainder --> 0 ---> Even 
# Remainder ---> 1 ---> Odd

number = int(input('Enter the No:'))
output = ['Even','Odd'] 
print('No is ',output[number%2])



    