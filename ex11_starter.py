#!/usr/bin/python
#define belgium variable
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#len is a function that returns the number of items in an object which in this case the object is a string so it returns the number of characters
print("~"*len(Belgium))

#split is a method that splits the string into a list using as a separator the ","
#the commas are removed
belgium_list = Belgium.split(',')
print(belgium_list)

#the join is a method that is used to turn a list into a string where each item in the list is separated with the defined separator, in this case a ":"
belgium_new = ":".join(belgium_list)
print(belgium_new)

#the int function makes sure that numbers are treated as integers so they are not concatenated as strings
#the population of belgium( belgium_list[1] )is accessed through an index from the list belgium_list
total = int(belgium_list[1]) + int(belgium_list[3])
print(total)







